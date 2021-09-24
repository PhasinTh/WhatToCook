<template>
  <el-row type="flex" justify="center">
    <el-col :sm="24" :lg="10">
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
    this.fetchData();
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
          this.ingredients = response.data.ingredients;
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
