<template>
  <el-form ref="form" :model="form" label-width="120px">
    <el-form-item label="No of meal">
      <el-input-number v-model="form.numberOfMeal" controls-position="right">
      </el-input-number>
    </el-form-item>
    <el-form-item label="No of calories">
      <el-input-number v-model="form.caloriesPreference" :precision="2" :step="0.25" :max="10"
        controls-position="right">
      </el-input-number>
    </el-form-item>
    <el-form-item label="No of cost">
      <el-input-number v-model="form.costPreference" :precision="2" :step="0.25" :max="10"
        controls-position="right">
      </el-input-number>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">Calculate</el-button>
      <el-button icon="el-icon-delete"></el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import http from '@/utils/http_client';

export default {
  data() {
    return {
      form: {
        numberOfMeal: 4,
        caloriesPreference: 0.2,
        costPreference: 0.8,
      },
    };
  },
  methods: {
    onSubmit() {
      http.post('process')
        .then((resopnse) => {
          this.$router.push({
            name: 'Result',
            params: {
              results: resopnse.data,
            },
          });
        })
        .catch((error) => console.log(error));
      console.log('submit!');
    },
  },
};

</script>
