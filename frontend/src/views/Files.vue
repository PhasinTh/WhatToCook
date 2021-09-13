<template>
  <div>
    <h1>Files</h1>
    <files-list @handleDelete="handleDelete" :files="files" />
    <br>
    <file-upload @handleUpload="fetchData" />
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
      files: null,
    };
  },
  methods: {
    fetchData() {
      http.get('files')
        .then((response) => {
          this.files = response.data.map((x) => ({
            name: x,
          }));
        })
        .catch((error) => console.log(error));
    },
    handleDelete(row) {
      http.post('files/delete', { filename: row.name })
        .then((response) => {
          console.log(response);
          this.fetchData();
        })
        .catch((error) => console.log(error));
    },
  },
};

</script>
