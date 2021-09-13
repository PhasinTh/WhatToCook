import Vue from 'vue';
import App from './App.vue';
import router from './router';
// import * as axios from './utils/http_request';
import './plugins/element';

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
