<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-lx-cascades"></i> 设备管理
        </el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div class="container">
      <div class="handle-box">
        <!-- <el-button
          type="primary"
          icon="el-icon-delete"
          class="handle-del mr10"
          @click="delAllSelection"
          >批量删除</el-button
        > -->

        <!-- 搜索功能 -->
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

          <!-- <div style="float: right"> -->
          <el-button
            v-if="user.role == 'manager'"
            style="margin: 0 20px 20px 0"
            type="primary"
            plain
            icon="el-icon-lx-add"
            @click="handleAdd"
          >
            新增设备
          </el-button>
          <!-- </div> -->
        </div>

        <!-- 筛选框 -->
        <div class="data-fliter-box">
          <el-form
            :inline="true"
            :model="searchForm"
            class="search-form-inline"
          >
            <el-form-item width="10px">
              <el-input
                v-model="searchForm.facID"
                placeholder="输入筛选ID"
                clearable
              ></el-input>
            </el-form-item>

            <el-form-item>
              <el-input
                v-model="searchForm.name"
                placeholder="输入筛选设备名"
                clearable
              ></el-input>
            </el-form-item>

            <el-form-item>
              <el-select
                v-model="searchForm.type"
                clearable
                placeholder="选择设备类型"
              >
                <el-option
                  v-for="item in typeOptions"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                >
                </el-option>
              </el-select>
            </el-form-item>

            <el-form-item>
              <el-select
                v-model="searchForm.status"
                clearable
                placeholder="选择设备状态"
              >
                <el-option
                  v-for="item in statusOptions"
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
      </div>

      <el-table
        :data="tableData"
        border
        class="table"
        ref="tableData"
        header-cell-class-name="table-header"
        element-loading-text="加载中……"
        :default-sort="{ prop: 'facID', order: 'ascending' }"
        @selection-change="handleSelectionChange"
      >
        <el-table-column type="selection" align="center"></el-table-column>

        <el-table-column
          prop="facID"
          label="ID"
          align="center"
          sortable
        ></el-table-column>

        <el-table-column
          prop="name"
          label="设备名"
          align="center"
          sortable
        ></el-table-column>

        <el-table-column label="设备类型" align="center" sortable>
          <template #default="scope">
            <el-tag effect="plain">{{
              scope.row.type === "temp"
                ? "环境温度"
                : scope.row.type === "bodyt"
                ? "患者体温"
                : scope.row.type === "humi"
                ? "空气湿度"
                : scope.row.type === "rate"
                ? "患者心率"
                : "其他"
            }}</el-tag>
          </template>
        </el-table-column>

        <el-table-column
          prop="unit"
          label="设备数据单位"
          align="center"
          sortable
        ></el-table-column>

        <el-table-column
          prop="step"
          label="时间步长"
          align="center"
          sortable
        ></el-table-column>

        <!-- <el-table-column label="账户余额">
          <template #default="scope">￥{{ scope.row.money }}</template>
        </el-table-column>
        <el-table-column label="头像(查看大图)" align="center">
          <template #default="scope">
            <el-image
              class="table-td-thumb"
              :src="scope.row.thumb"
              :preview-src-list="[scope.row.thumb]"
            ></el-image>
          </template>
        </el-table-column> -->

        <el-table-column label="设备状态" align="center">
          <template #default="scope">
            <el-tag
              :type="
                scope.row.status === 'online'
                  ? 'success'
                  : scope.row.status === 'offline'
                  ? 'info'
                  : 'danger'
              "
              >{{
                scope.row.status === "online"
                  ? "在线"
                  : scope.row.status === "offline"
                  ? "离线"
                  : "出错"
              }}</el-tag
            >
          </template>
        </el-table-column>

        <el-table-column
          label="操作"
          v-if="user.role == 'manager'"
          align="center"
        >
          <template #default="scope">
            <el-button
              type="text"
              icon="el-icon-edit"
              @click="handleEdit(scope.$index, scope.row)"
              >编辑</el-button
            >
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

    <!-- 编辑弹出框 -->
    <el-dialog title="编辑" v-model="editVisible" width="40%">
      <el-form
        ref="editForm"
        :model="editForm"
        :rules="formRules"
        label-width="150px"
      >
        <el-form-item prop="facID" label="ID">
          <el-input disabled v-model="editForm.facID"></el-input>
        </el-form-item>

        <el-form-item prop="name" label="设备名">
          <el-input v-model="editForm.name"></el-input>
        </el-form-item>

        <el-form-item prop="type" label="设备类型">
          <el-select v-model="editForm.type">
            <el-option
              v-for="item in typeOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            >
            </el-option>
          </el-select>
        </el-form-item>

        <el-form-item prop="unit" label="数据单位">
          <el-input v-model="editForm.unit"></el-input>
        </el-form-item>

        <el-form-item prop="step" label="时间步长">
          <el-input v-model="editForm.step">
            <template v-slot:append>min</template>
          </el-input>
        </el-form-item>

        <el-form-item prop="status" label="设备状态">
          <el-select v-model="editForm.status">
            <el-option
              v-for="item in statusOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            >
            </el-option>
          </el-select>
        </el-form-item>
      </el-form>

      <template #footer>
        <span class="dialog-footer">
          <!-- <el-button @click="debug_cancelEdit()">取 消</el-button> -->
          <el-button @click="editVisible = false">取 消</el-button>
          <el-button type="primary" @click="saveEdit()">确 定</el-button>
        </span>
      </template>
    </el-dialog>

    <!-- 新增弹出框 -->
    <el-dialog title="新增设备" v-model="addVisible" width="40%">
      <el-form
        ref="addForm"
        :model="addForm"
        :rules="formRules"
        label-width="150px"
      >
        <!-- <el-form-item label="ID">
          <el-input disabled v-model="addForm.facID"></el-input>
        </el-form-item> -->

        <el-form-item prop="name" label="设备名">
          <el-input
            v-model="addForm.name"
            placeholder="请输入设备名"
          ></el-input>
        </el-form-item>

        <el-form-item prop="type" label="设备类型">
          <el-select v-model="addForm.type">
            <el-option
              v-for="item in typeOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            >
            </el-option>
          </el-select>
        </el-form-item>

        <el-form-item prop="unit" label="数据单位">
          <el-input
            v-model="addForm.unit"
            placeholder="请输入设备的单位"
          ></el-input>
        </el-form-item>

        <el-form-item prop="step" label="时间步长">
          <el-input v-model="addForm.step" placeholder="请输入设备时间步长">
            <template v-slot:append>min</template>
          </el-input>
        </el-form-item>

        <el-form-item prop="status" label="设备状态">
          <el-select v-model="addForm.status">
            <el-option
              v-for="item in statusOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            >
            </el-option>
          </el-select>
        </el-form-item>
      </el-form>

      <template #footer>
        <span class="dialog-footer">
          <el-button @click="addVisible = false">取 消</el-button>
          <el-button type="primary" @click="saveAdd()">确 定</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script>
// import { fetchData } from "@/api/index.js";
import { formatJson } from "@/utils/utils";
import {
  getAllFacility,
  removeFacility,
  updateFacility,
  addFacility,
} from "@/api/facility";
export default {
  name: "facility",
  data() {
    return {
      // 导出excel按钮状态
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
      // 数据筛选相关
      searchForm: {
        facID: "",
        name: "",
        type: "", // 选择
        status: "", // 选择
      },
      // 数据修改相关
      editVisible: false,
      editForm: {
        name: "",
        type: "temp",
        status: "online",
        unit: "",
        step: "",
      },
      addVisible: false,
      addForm: {
        name: "",
        type: "temp",
        status: "online",
        unit: "",
        step: "",
      },
      formRules: {
        name: [{ required: true, message: "请输入设备名", trigger: "blur" }],
        type: [{ required: true, message: "请选择设备类型", trigger: "blur" }],
        status: [
          { required: true, message: "请选择设备状态", trigger: "blur" },
        ],
        unit: [
          {
            required: true,
            message: "请输入数据单位，如：摄氏度、%",
            trigger: "blur",
          },
        ],
        step: [
          { required: true, message: "请输入时间步长", trigger: "blur" },
          {
            pattern: /^[1-9][0-9]*([.][0-9]+)?$/,
            message: "时间步长必须为非零开头的实数",
            trigger: "blur",
          },
        ],
      },
      // enum类型数据
      typeOptions: [
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
      statusOptions: [
        {
          value: "online",
          label: "online",
        },
        {
          value: "offline",
          label: "offline",
        },
        {
          value: "error",
          label: "error",
        },
      ],
      // 通过api从数据库获取的原始数据
      originalData: [
        {
          facID: "5211",
          name: "hello初代机",
          type: "temp",
          status: "online",
          unit: "摄氏度",
          step: "10",
        },
        {
          facID: "3699",
          name: "hello二号机",
          type: "humi",
          status: "offline",
          unit: "%",
          step: "60",
        },
        {
          facID: "8888",
          name: "hello三号机",
          type: "bodyt",
          status: "error",
          unit: "摄氏度",
          step: "1",
        },
      ],
    };
  },
  created() {
    this.getOriginalData();
  },
  computed: {
    // 根据筛选条件确定的表格中的数据
    tableData() {
      return this.originalData.filter((item) => {
        return (
          item.facID.includes(this.searchForm.facID) &&
          item.name.includes(this.searchForm.name) &&
          item.type.includes(this.searchForm.type) &&
          item.status.includes(this.searchForm.status)
        );
      });
    },
  },
  methods: {
    // 导出excel逻辑
    handleExportExcel() {
      this.exportingExcel = true;
      import("@/vendor/Export2Excel").then((excel) => {
        const tHeader = [
          "ID",
          "设备名",
          "设备类型",
          "设备状态",
          "设备数据单位",
          "设备时间步长(min)",
        ];
        const filterVal = ["facID", "name", "type", "status", "unit", "step"];
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
      });
    },
    // 多选逻辑
    handleSelectionChange(val) {
      // console.log("handleSelectionChange");
      // console.log(val);
      this.selectedData = val;
    },
    // 获取originalData
    getOriginalData() {
      getAllFacility()
        .then((res) => {
          // console.log("getAllFacility");
          // console.log(res.data);
          this.originalData = res.data.list;
        })
        .catch(() => {
          this.$message.error("getAllFacility后端服务器超时");
        });
    },

    // 编辑 / 删除逻辑
    handleDelete(index, row) {
      this.$confirm("确定要删除吗？", "提示", {
        type: "warning",
      })
      .then(() => {
        const data = { facID: row.facID };
        removeFacility(data)
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
            this.$message.error("removeFacility后端服务器超时");
          });
      })
      .catch(() => {});
    },
    handleEdit(index, row) {
      this.editForm = JSON.parse(JSON.stringify(row));
      this.editVisible = true;
    },
    saveEdit() {
      this.$refs["editForm"].validate((valid) => {
        if (valid) {
          this.editVisible = false;
          const submit_data = this.editForm;
          updateFacility(submit_data)
            .then((res) => {
              if (res.data.ifTrue) {
                this.$message.success("修改设备 ${this.editForm.facID} 成功");
                // TODO 前后端连接后 测试修改是否成功
                this.getOriginalData(); // 刷新数据
              } else {
                this.$message.error("修改失败");
              }
            })
            .catch((e) => {
              console.log(e);
              this.$message.error("removeFacility后端服务器超时");
            });
        } else {
          this.$message.error("您提交的数据不合规范，请检查后再试。");
        }
      });
    },
    // Just for DEBUG
    debug_cancelEdit() {
      this.editVisible = false;
      // console.log("cancel edit");
      // console.log("editForm---------------");
      // console.log(this.editForm);
      // console.log("tableData---------------");
      // console.log(this.tableData);
      // console.log("originalData---------------");
      // console.log(this.originalData);
    },
    handleAdd() {
      this.addVisible = true;
    },
    saveAdd() {
      this.$refs.addForm.validate((valid) => {
        if (valid) {
          this.addVisible = false;
          const submit_data = this.addForm;
          // console.log("正在提交新增设备表单");
          // console.log(submit_data);
          addFacility(submit_data)
            .then((res) => {
              // console.log("这是服务器返回的结果");
              // console.log(res);
              if (res.data.ifTrue) {
                const newID = res.data.info.facID;
                console.log(newID);
                this.$message.success("增加设备 ${newID} 成功");
                // TODO 前后端连接后 测试修改是否成功

                // 提交成功后，清空addForm
                this.addForm = {
                  name: "",
                  type: "temp",
                  status: "online",
                  unit: "",
                  step: "",
                };
                this.getOriginalData(); // 刷新数据
              } else {
                this.$message.error("增加失败");
              }
            })
            .catch((e) => {
              console.log(e);
              this.$message.error("updateFacility后端服务器超时");
            });
        } else {
          return false;
        }
      });
    },
  },
};
</script>

<style scoped>
.el-form-item .el-input {
  width: 200px;
}
.el-form-item .el-select {
  width: 200px;
}

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

@media screen and (max-width: 1200px) {
  .el-form-item .el-input {
    width: 150px;
  }
  .el-form-item .el-select {
    width: 150px;
  }
  .el-dialog {
    width: "40%";
  }
}

@media screen and (max-width: 850px) {
  .el-form-item .el-input {
    width: 100px;
  }
  .el-form-item .el-select {
    width: 100px;
  }
  .el-dialog {
    width: "80%";
  }
}
</style>
