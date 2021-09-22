<template>
  <div id="app">
    <el-header style="margin-top: 1rem;height: 50px;" align="right">
      <Navbar />
    </el-header>
    <el-container>
      <el-main style="padding-top: 0;">
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

html {
  height: 100%;
}

body {
  background-color: #fff;
  background-image: url("assets/images/background.png");
  /* background-repeat: no-repeat; */
  /* background-size: fill; */
  margin: 0;
  padding: 0;
}

.el-button {
  /* margin-top: 1rem!important; */
  padding-left: 2.5rem!important;
  padding-right: 2.5rem!important;
}

.el-button--primary {
  /* background-color: lightseagreen  !important; */
  /* border-color: lightseagreen  !important; */

  background-color: #19be9b !important;
  border-color: #19be9b !important;
}

.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n+1) {
  background-color: #d3dce6;
}

.el-slider__bar {
  /* background-color: lightseagreen !important; */
  background-color: #19be9b !important;
}

.el-slider__button{
  /* border-color: lightseagreen !important; */
  border-color: #19be9b !important;
}

.el-slider {
  margin-left: 15%;
  margin-right: 15%;
}

.el-slider__marks-text {
  margin-top: 5px !important;
}

.el-input__inner {
  font-size: medium!important;
}

.el-form-item {
  margin-bottom: 2.5rem!important;
}

.el-form-item__label {
  font-size: x-large!important;
}

.text-xlarge {
  font-size: x-large;
}
.text-large {
  font-size: large;
}

.text-medium {
  font-size: medium;
}

.text-small {
  font-size: small;
}
</style>
