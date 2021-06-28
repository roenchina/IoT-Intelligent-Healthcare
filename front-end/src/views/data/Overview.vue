<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-lx-calendar"></i> 数据查询
        </el-breadcrumb-item>
        <el-breadcrumb-item> 数据总览 </el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div class="container">
      <div class="export-excel-box">
        <el-button
          :loading="exportingExcel"
          style="margin: 0 20px 20px 0"
          type="primary"
          icon="el-icon-document"
          @click="handleExportExcel()"
        >
          导出已选数据为Excel表
        </el-button>

        <!-- <el-button
          v-if="user.role == 'manager'"
          style="margin: 0 20px 20px 0"
          type="primary"
          plain
          icon="el-icon-lx-add"
          @click="handleAdd"
        >
          新增设备
        </el-button> -->
      </div>

      <div class="data-fliter-box">
        <el-form :inline="true" :model="searchForm" class="search-form-inline">
          <el-form-item>
            <el-input
              v-model="searchForm.time"
              placeholder="输入筛选时间"
              clearable
            ></el-input>
          </el-form-item>

          <el-form-item>
            <el-input
              v-model="searchForm.location"
              placeholder="输入筛选方位"
              clearable
            ></el-input>
          </el-form-item>

          <el-form-item>
            <el-select
              v-model="searchForm.facType"
              clearable
              placeholder="选择数据类型"
            >
              <el-option
                v-for="item in facTypeOptions"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              >
              </el-option>
            </el-select>
          </el-form-item>

          <el-form-item>
            <el-select
              v-model="searchForm.type"
              clearable
              placeholder="选择是否正常"
            >
              <el-option
                v-for="item in dataTypeOptions"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              >
              </el-option>
            </el-select>
          </el-form-item>

          <el-form-item>
            <el-button icon="el-icon-search" circle disabled></el-button>
          </el-form-item>
        </el-form>
      </div>

      <el-table
        :data="tableData"
        ref="tableData"
        border
        class="table"
        header-cell-class-name="table-header"
        element-loading-text="加载中……"
        :default-sort="{ prop: 'time', order: 'descending' }"
        @selection-change="handleSelectionChange"
      >
        <el-table-column
          type="selection"
          align="center"
        ></el-table-column>

        <el-table-column
          prop="_ID"
          label="ID"
          align="center"
          sortable
        ></el-table-column>

        <el-table-column
          prop="time"
          label="时间"
          align="center"
          sortable
        ></el-table-column>

        <el-table-column
          prop="facID"
          label="设备号"
          align="center"
          sortable
        ></el-table-column>

        <!-- <el-table-column
          prop="wardID"
          label="病房号"
          align="center"
          sortable
        ></el-table-column> -->

        <el-table-column
          prop="location"
          label="方位"
          align="center"
          sortable
        ></el-table-column>

        <el-table-column label="具体数值" align="center">
          <template #default="scope"
            >{{ scope.row.amount }} {{ scope.row.unit }}</template
          >
        </el-table-column>

        <el-table-column label="数据类型" align="center" sortable>
          <template #default="scope">
            <el-tag effect="plain">{{
              scope.row.facType === "temp"
                ? "环境温度"
                : scope.row.facType === "bodyt"
                ? "患者体温"
                : scope.row.facType === "humi"
                ? "空气湿度"
                : scope.row.facType === "rate"
                ? "患者心率"
                : "其他"
            }}</el-tag>
          </template>
        </el-table-column>

        <el-table-column label="是否正常" align="center">
          <template #default="scope">
            <el-tag
              :type="
                scope.row.type === 'normal'
                  ? 'success'
                  : scope.row.type === 'warning'
                  ? 'danger'
                  : ''
              "
              >{{ scope.row.type }}</el-tag
            >
          </template>
        </el-table-column>

        <!-- 管理员权限：编辑、删除 -->
        <el-table-column
          v-if="user.role === 'manager'"
          label="管理员操作"
          width="180"
          align="center"
        >
          <template #default="scope">
            <!-- <el-button
              type="text"
              icon="el-icon-edit"
              @click="handleEdit(scope.$index, scope.row)"
              >编辑</el-button
            > -->
            <el-button
              type="text"
              icon="el-icon-delete"
              class="red"
              @click="handleDelete(scope.$index, scope.row)"
              >删除</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
// import { fetchData } from "@/api/index.js";
import { formatJson } from "@/utils/utils";
import { getAllData, deleteData } from "@/api/data.js";
export default {
  name: "basetable",
  data() {
    return {
      // 导出excel的按钮状态
      exportingExcel: false,
      // 前端勾选的数据
      selectedData: [],
      // 用户相关
      user: {
        ID: localStorage.getItem("ls_userID"),
        name: localStorage.getItem("ls_userName"),
        role: localStorage.getItem("ls_userRole"),
        email: localStorage.getItem("ls_userEmail"),
      },
      searchForm: {
        time: "", // 时间选择器
        location: "",
        type: "", // 选择：normal / warning
        facType: "", // 选择
      },
      dataTypeOptions: [
        {
          value: "normal",
          label: "normal",
        },
        {
          value: "warning",
          label: "warning",
        },
      ],
      facTypeOptions: [
        {
          value: "temp",
          label: "温度",
        },
        {
          value: "humi",
          label: "湿度",
        },
        {
          value: "bodyt",
          label: "体温",
        },
        {
          value: "rate",
          label: "心率",
        },
      ],
      originalData: [
        // {
        //   _ID: "10001",
        //   facID: "5211",
        //   time: "2021-6-23",
        //   location: "est",
        //   type: "normal", // normal / warning
        //   amount: "37.2",
        //   unit: "摄氏度", // 需要根据facID查找
        //   facType: "体温",
        // },
        // {
        //   _ID: "10008",
        //   facID: "002",
        //   time: "2020-2-1",
        //   location: "wst",
        //   type: "warning",
        //   amount: "38.9",
        //   unit: "摄氏度",
        //   facType: "体温",
        // },
      ],
    };
  },
  created() {
    this.getOriginalData();
  },
  computed: {
    tableData() {
      return this.originalData.filter((item) => {
        return (
          item.time.includes(this.searchForm.time) &&
          item.location.includes(this.searchForm.location) &&
          item.facType.includes(this.searchForm.facType) &&
          item.type.includes(this.searchForm.type)
        );
      });
    },
  },
  methods: {
    handleExportExcel() {
      this.exportingExcel = true;
      import("@/vendor/Export2Excel")
        .then((excel) => {
          const tHeader = [
            "数据ID",
            "发送时间",
            "设备ID",
            "位置",
            "是否正常",
            "具体数值",
            "数据单位",
            "数据类型",
          ];
          const filterVal = [
            "_ID",
            "time",
            "facID",
            "location",
            "type",
            "amount",
            "unit",
            "facType",
          ];
          const list = this.selectedData;
          const data = formatJson(filterVal, list);
          excel.export_json_to_excel({
            header: tHeader,
            data,
            filename: this.filename,
            autoWidth: this.autoWidth,
            bookType: this.bookType,
          });
          this.exportingExcel = false;
        })
        .catch((e) => {
          console.log(e);
          this.$message.error("导出时出错，请稍后再试");
          this.exportingExcel = false;
        });
    },
    handleSelectionChange(val) {
      // console.log("handleSelectionChange");
      // console.log(val);
      this.selectedData = val;
    },
    getOriginalData() {
      const params = {
        limit: 100,
        sort: "recent",
      };
      getAllData(params)
        .then((res) => {
          // console.log("---in getAllData---");
          // console.log(res.data);
          // this.originalData = res.data.list;
          this.originalData = res.data;
        })
        .catch((e) => {
          console.log(e);
          this.$message.error("getAllData后端服务器超时");
        });
    },
    handleDelete(index, row) {
      this.$confirm("确定要删除吗？", "提示", {
        type: "warning",
      })
      .then(() => {
        const data = { _ID: row._ID };
        deleteData(data)
          .then((res) => {
            if (res.data.ifTrue) {
              this.$message.success("删除成功");
              // this.originalData.splice(index, 1);
              // TODO 测试删除是否成功
              this.getOriginalData();
            } else {
              this.$message.error("删除失败");
            }
          })
          .catch((e) => {
            console.log(e);
            this.$message.error("deleteData后端服务器超时");
          });
      })
      .catch(() => {});
    },
  },
};
</script>

<style scoped>
.handle-box {
  margin-bottom: 20px;
}

.handle-select {
  width: 120px;
}

.handle-input {
  width: 300px;
  display: inline-block;
}
.table {
  width: 100%;
  font-size: 14px;
}
.red {
  color: #ff0000;
}
.mr10 {
  margin-right: 10px;
}
.table-td-thumb {
  display: block;
  margin: auto;
  width: 40px;
  height: 40px;
}
</style>
