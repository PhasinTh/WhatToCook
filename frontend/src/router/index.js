import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/files',
    name: 'Files',
    component: () => import(/* webpackChunkName: "files" */ '../views/Files.vue'),
  },
  {
    path: '/result/:planId',
    name: 'Result',
    component: () => import(/* webpackChunkName: "files" */ '../views/Result.vue'),
    props: true,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
