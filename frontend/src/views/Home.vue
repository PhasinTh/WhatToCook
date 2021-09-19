<template>
  <el-row type="flex" :gutter="24" justify="center">
    <el-col :sm="24" :md="10">
      <div class="card-container">
        <h1>List of ingredients</h1>
        <IngredientList />
      </div>
    </el-col>
    <el-col :sm="24" :md="10">
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

export default {
  name: 'Home',
  components: {
    Form,
    IngredientList,
  },
};
</script>
