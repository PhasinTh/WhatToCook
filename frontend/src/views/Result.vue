<template>
  <el-row type="flex" justify="center">
    <el-col :md="20">
      <div class="card-container">
          <h1>Results</h1>
          {{ results }}
          <div>
            <el-button
              type="primary"
              icon="el-icon-back"
              @click="$router.back()"></el-button>
          </div>
      </div>
    </el-col>
    </el-row>
</template>

<script>
export default {
  props: ['results'],
};
</script>

<style>
.el-button {
  padding-left: 2.5rem;
  padding-right: 2.5rem;
}
</style>
