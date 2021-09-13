<template>
  <div id="app">
    <el-container style="background-color: white;">
      <el-header>
        <router-link to="/">Home</router-link> |
        <router-link to="/files">Files</router-link>
      </el-header>
      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

body {
  background-image: url('assets/images/background.jpg');;
}
</style>
