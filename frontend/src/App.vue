<template>
  <div id="app">
    <Navbar />
    <el-container>
      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';

export default {
  components: {
    Navbar,
  },
};
</script>

<style>
#app {
  font-family: 'Handlee';font-size: 22px;
  text-align: center;
  color: #2c3e50;
  font-size: 150%;
}

body {
  background-color: #eee;
  background-image: url("assets/images/background.png");
  margin: 0;
  padding: 0;
}

.card-container {
  background-color: white;
  padding: 0.5rem;
  height: 100%;
}

</style>
