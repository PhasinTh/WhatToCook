<template>
  <el-form ref="form" :model="form" label-width="120px" label-position="top">
    <el-form-item label="Number of Meal">
      <el-input-number v-model="form.numberOfMeal" :min="0"></el-input-number>
    </el-form-item>
    <el-form-item :label="`Calories Preference (0-1) : ${form.caloriesPreference}`">
      <el-slider
        v-model="form.caloriesPreference"
        :min="0"
        :max="1"
        :step="0.05"
        :marks="{ 0: '0', 0.5: '0.5', 1: '1' }"
      ></el-slider>
    </el-form-item>

    <el-form-item :label="`Cost Preference (0-1) : ${form.costPreference}`">
      <el-slider
        v-model="form.costPreference"
        :min="0"
        :max="1"
        :step="0.05"
        :marks="{ 0: '0', 0.5: '0.5', 1: '1' }"
      ></el-slider>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">Calculate</el-button>
      <el-button icon="el-icon-delete" @click="onClear">Clear</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import http from '@/utils/http_client';

export default {
  data() {
    return {
      form: {
        numberOfMeal: 1,
        caloriesPreference: 0.5,
        costPreference: 0.5,
      },
    };
  },
  methods: {
    onSubmit() {
      http.post('plan')
        .then((resopnse) => {
          this.$router.push({
            name: 'Result',
            params: {
              planId: resopnse.data,
            },
          });
        })
        .catch((error) => console.log(error));
    },
    onClear() {
      this.form = {
        numberOfMeal: 1,
        caloriesPreference: 0.5,
        costPreference: 0.5,
      };
    },
  },
};

</script>
