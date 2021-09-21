<template >
  <el-row :gutter="8">
    <el-col :md="8" v-for="item in ingredients" :key="item.id" style="margin-bottom: .5rem;">
    <el-card shadow="hover">
      <el-row >
        <el-col :span="6" align="center" >
          <el-avatar shape="square"
          :size="36"
          src="@/assets/images/default_icon.png"
          >
          <img :src="item.url"/>
        </el-avatar>
        </el-col>
        <el-col :span="18" align="left" style="padding-left: 0.5rem;">
          <b>{{ item.quantity || 1 }} x {{ item.name }} </b> <br>
          {{ item.calories }} cal. cost:{{ item.cost }}
        </el-col>
      </el-row>
      </el-card>
    </el-col>
  </el-row>
</template>
<script>
export default {
  props: ['ingredients'],
};
</script>

<style>
.el-avatar {
  background-color: #FFF !important;
}

</style>
