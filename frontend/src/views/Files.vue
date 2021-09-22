<template>
  <div>
    <el-row type="flex" justify="center">
      <el-col :md="16">
        <h1>Files</h1>
        <files-list @handleDelete="handleDelete"
          :files="files"
          :loading="loading"
          style="min-height: 30vh" />
      </el-col>
    </el-row>
    <el-row type="flex" justify="center" style="margin-top: .5rem;">
        <el-col :md="16">
          <file-upload @handleUpload="fetchData" v-if="!loading" />
        </el-col>
    </el-row>
  </div>
</template>

<script>
import FilesList from '@/components/FilesList.vue';
import FileUpload from '@/components/FileUpload.vue';
import http from '@/utils/http_client';

export default {
  components: { FilesList, FileUpload },
  created() {
    this.fetchData();
  },
  data() {
    return {
      loading: false,
      files: null,
    };
  },
  methods: {
    fetchData() {
      this.loading = true;
      http.get('files')
        .then((response) => {
          this.files = response.data.map((x) => ({
            name: x,
          }));
          this.loading = false;
        })
        .catch((error) => {
          console.log(error);
          this.$notify.error({
            title: 'Error',
            message: 'Can\'t connect to the server',
          });
        });
    },
    handleDelete(row) {
      http.post('files/delete', { filename: row.name })
        .then((response) => {
          console.log(response);
          this.fetchData();
          this.$notify({
            title: 'Success',
            message: 'Success to add file.',
            type: 'success',
          });
        })
        .catch((error) => console.log(error));
    },
  },
};

</script>
