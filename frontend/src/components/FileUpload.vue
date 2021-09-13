<template>
  <el-upload drag action="http://localhost:5000/files"
    :on-success="handleSuccess" :file-list="fileList">
    <i class="el-icon-upload"></i>
    <div class="el-upload__text">Drop file here or <em>click to upload</em></div>
    <!-- <div class="el-upload__tip" slot="tip">jpg/png files with a size less than 500kb</div> -->
  </el-upload>
</template>
s
<script>
export default {
  name: 'FileUpload',
  data() {
    return {
      fileList: [],
    };
  },
  methods: {
    handleSuccess(file, fileList) {
      console.log(file, fileList);
      this.$emit('handleUpload');
    },
  },
};

</script>
