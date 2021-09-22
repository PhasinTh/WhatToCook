<template>
  <div>
    <router-link to="/" class="default-link">Home</router-link> |
    <router-link to="/files" class="default-link">Files</router-link>
  </div>
</template>

<style scoped>
  .default-link {
    text-decoration: none;
    color: #000;
    font-size: xx-large;
  }
  .default-link:hover {
    color: lightseagreen !important;
  }

</style>
