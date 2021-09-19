<template>
  <el-header>
    <router-link to="/" class="default-link">Home</router-link> |
    <router-link to="/files" class="default-link">Files</router-link>
  </el-header>
</template>

<style scoped>
  .default-link {
    text-decoration: none;
    color: #000;
    font-size: larger;
  }
  .default-link:hover {
    color: #409EFF;
  }

</style>
