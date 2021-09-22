<template>
  <el-row type="flex" justify="center">
    <el-col :md="20" >
      <div class="card-container">
          <h1>Recommended menu</h1>
          <div v-loading="loading">
            <el-carousel type="card"
              height="28vh"
              :autoplay="false"
              :loop="true"
              @change="onChangeHandler"
              trigger="false">
              <el-carousel-item
                v-for="(menu, index) in plan.menu"
                :key="menu.id"
                :style="{ backgroundColor: bgColors[index], color: 'white', fontWeight: 'bold'}">
                <el-image
                  style="width: 150px; height: 150px"
                  :src="menu.url"
                  ></el-image>
                <br>
                <span class="text-xlarge">{{ menu.name }}</span>
                <br>
                <p class="text-medium">
                  Total Cal: {{ menu.total_cal }}
                  |
                  Total Cost: {{ menu.total_cost }}
                </p>
              </el-carousel-item>
            </el-carousel>
          </div>

          <h1>ShoppingList</h1>
          <div>
            <IngredientList :ingredients="plan.menu[activeItem].shoppingList" :cols="4" />
          </div>
          <el-button
            type="primary"
            icon="el-icon-back"
            @click="$router.back()">
          </el-button>
      </div>
    </el-col>
    </el-row>
</template>

<script>
import http from '@/utils/http_client';
import IngredientList from '../components/IngredientList.vue';

export default {
  props: ['planId'],
  components: {
    IngredientList,
  },
  data() {
    return {
      loading: false,
      bgColors: ['#19be9b', '#3296dc', '#9b5ab4', '#f0c30f', '#e67d23', '#e64b3c'],
      activeItem: 0,
      plan: [],
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      // this.loading = true;
      http.get(`plan/${this.planId}`)
        .then((response) => {
          this.plan = response.data;
          console.log(response.data);
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
    onChangeHandler(active) {
      this.activeItem = active;
    },
  },
};
</script>
