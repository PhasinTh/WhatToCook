<template>
  <el-row type="flex" :gutter="24" justify="center" >
    <el-col :sm="24" :lg="10" >
      <div class="card-container">
        <h1>List of ingredients</h1>
        <IngredientList :ingredients="ingredients" v-loading="loading" />
      </div>
    </el-col>
    <el-col :sm="24" :lg="10">
      <div class="card-container">
        <h1>Enter......</h1>
        <Form />
      </div>
    </el-col>
  </el-row>
</template>

<script>
import Form from '@/components/Form.vue';
import IngredientList from '../components/IngredientList.vue';
import http from '@/utils/http_client';

export default {
  name: 'Home',
  components: {
    Form,
    IngredientList,
  },
  created() {
    // this.fetchData();
    this.ingredients = [{
      name: 'almond', calories: 68, cost: 105, url: 'almond.png',
    }, {
      name: 'apple', calories: 87, cost: 397, url: 'apple.png',
    }, {
      name: 'bacon', calories: 20, cost: 639, url: 'bacon.png',
    }, {
      name: 'basil', calories: 17, cost: 996, url: 'basil.png',
    }, {
      name: 'bay', calories: 47, cost: 235, url: 'bay.png',
    }, {
      name: 'beans', calories: 75, cost: 544, url: 'beans.png',
    }, {
      name: 'beef', calories: 35, cost: 217, url: 'meat.png',
    }, {
      name: 'bread', calories: 77, cost: 563, url: 'bread.png',
    }];
  },
  data() {
    return {
      ingredients: [],
      loading: false,
    };
  },
  methods: {
    fetchData() {
      this.loading = true;
      http.get('ingredients')
        .then((response) => {
          this.ingredients = response.data;
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
  },
};
</script>
