<template>
    <div>
        <h1>Results</h1>
        {{ results }}

        <div>
          <el-button type="primary" icon="el-icon-back" @click="$router.back()"></el-button>
        </div>
    </div>
</template>

<script>
export default {
  props: ['results'],
};
</script>
