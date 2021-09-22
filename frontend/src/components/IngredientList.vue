<template >
  <el-row :gutter="8">
    <el-col
      :md="cols ? 24/cols : 12"
      v-for="item in ingredients"
      :key="item.id"
      style="margin-bottom: .5rem;">
    <el-card shadow="hover">
      <el-row >
        <el-col :span="4" align="center" >
          <el-avatar shape="square"
          :size="36"
          :src="item.url"
          >
          <img src="@/assets/images/default_icon.png"/>
        </el-avatar>
        </el-col>
        <el-col :span="20" align="left" style="padding-left: 0.5rem;">
          <b>{{ item.quantity || 1 }} x {{ item.name }} </b> <br>
          Cal: <b>{{ item.calories }}</b>  Cost: <b>{{ item.cost }}</b>
        </el-col>
      </el-row>
      </el-card>
    </el-col>
  </el-row>
</template>
<script>
export default {
  props: ['ingredients', 'cols'],
};
</script>

<style>
.el-avatar {
  background-color: #fff !important;
}
</style>
