<template>
  <el-table
    v-loading="loading"
    stripe
    :data="files"
    style="width: 100%">
    <el-table-column label="Name" header-align="center" align="center">
      <template slot-scope="scope">
        <el-popover trigger="hover" placement="top">
          <p>Name: {{ scope.row.name }}</p>
          <div slot="reference" class="name-wrapper">
            <el-tag size="medium">{{ scope.row.name }}</el-tag>
          </div>
        </el-popover>
      </template>
    </el-table-column>
    <el-table-column label="Action" header-align="center" align="center">
      <template slot-scope="scope">
        <el-button size="mini" type="danger"
          @click="$emit('handleDelete', scope.row)">
          Delete
        </el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
export default {
  props: ['files', 'loading'],
};

</script>
