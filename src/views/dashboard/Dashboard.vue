<template>
  <div class="dashboard-container">

<!-- row-1: info-card -->
    <el-row :gutter="20">
      <el-col :xs="24" :sm="8" :lg="8">
        <el-card shadow="hover" class="user-info-card">
          <div class="user-info">
            <div class="user-info-cont">
              <div class="user-info-name">欢迎，{{ user.name }}</div>
              <!-- <div>{{ userRole }}</div> -->
            </div>
          </div>
          <div class="user-info-list">
            您的账号是：
            <span>{{ user.ID }}</span>
          </div>
          <div class="user-info-list">
            您的身份是：
            <span>{{ user.role }}</span>
          </div>
          <div class="user-info-list">
            注册邮箱：
            <span>{{ user.email }}</span>
          </div>
        </el-card>
      </el-col>

      <el-col :xs="24" :sm="16" :lg="16">
        <el-card shadow="hover" class="clock-card">
          <template #header>
            <div class="clearfix">
              <span>当前的时间是——</span>
            </div>
          </template>
          <div class="time-div">
            <div>{{ nowDate }}</div>
            <div class="exact-time">{{ nowTime }}</div>
          </div>

          <!-- Vue
          <el-progress :percentage="71.3" color="#42b983"></el-progress
          >JavaScript
          <el-progress :percentage="24.1" color="#f1e05a"></el-progress>CSS
          <el-progress :percentage="13.7"></el-progress>HTML
          <el-progress :percentage="5.9" color="#f56c6c"></el-progress> -->
        </el-card>
      </el-col>
    </el-row>

<!-- row2: basic statics -->
    <el-row :gutter="20">
      <el-col :span="24">
        <el-row :gutter="20" class="mgb20">
          <el-col :xs="24" :sm="12" :lg="6">
            <el-card shadow="hover" :body-style="{ padding: '0px' }">
              <div class="grid-content grid-con">
                <i class="el-icon-lx-punch grid-con-icon"></i>
                <div class="grid-cont-right">
                  <div class="grid-num">{{ basic.facNum }}</div>
                  <div>总设备数</div>
                </div>
              </div>
            </el-card>
          </el-col>

          <el-col :xs="24" :sm="12" :lg="6">
            <el-card shadow="hover" :body-style="{ padding: '0px' }">
              <div class="grid-content grid-con">
                <i class="el-icon-lx-comment grid-con-icon"></i>
                <div class="grid-cont-right">
                  <div class="grid-num">{{ basic.dataNum }}</div>
                  <div>总数据量</div>
                </div>
              </div>
            </el-card>
          </el-col>

          <el-col :xs="24" :sm="12" :lg="6">
            <el-card shadow="hover" :body-style="{ padding: '0px' }">
              <div class="grid-content grid-con">
                <i class="el-icon-lx-people grid-con-icon"></i>
                <div class="grid-cont-right">
                  <div class="grid-num">{{ basic.patientNum }}</div>
                  <div>患者总数</div>
                </div>
              </div>
            </el-card>
          </el-col>

          <el-col :xs="24" :sm="12" :lg="6">
            <el-card shadow="hover" :body-style="{ padding: '0px' }">
              <div class="grid-content grid-con">
                <i class="el-icon-lx-home grid-con-icon"></i>
                <div class="grid-cont-right">
                  <div class="grid-num">{{ basic.wardNum }}</div>
                  <div>病房数量</div>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </el-col>
    </el-row>

<!-- row3: echarts -->
    <el-row :gutter="20">
      <el-col :xs="24" :sm="15" :lg="15">
        <el-card class="echats-card" shadow="hover">
          <template #header>
            <div class="clearfix">
              <span>折线图</span>
            </div>
          </template>

          <div class="line-chart">
            <v-chart class="chart" :option="option" />
          </div>
        </el-card>
      </el-col>

      <el-col :xs="24" :sm="9" :lg="9">
        <el-card class="echats-card" shadow="hover">
          <template #header>
            <div class="clearfix">
              <span>饼图</span>
            </div>
          </template>
          <div class="pie-chart">
            <v-chart class="chart" :option="option" />
          </div>
        </el-card>
      </el-col>

    </el-row>

<!-- row4: data-tables -->
    <el-row :gutter="20">
      <el-col :span="24">
        <el-card shadow="hover" style="height: 400px">
          <template #header>
            <div class="clearfix">
              <span>最新数据记录</span>
              <!-- <el-button style="float: right; padding: 3px 0" type="text"
                >添加</el-button
              > -->
            </div>
          </template>

          <el-table
            :data="recentData"
            :default-sort="{ prop: 'time', order: 'descending' }"
            border
            class="table"
            ref="multipleTable"
            header-cell-class-name="table-header"
          >
            <!-- <el-table-column
              type="selection"
              align="center"
              v-if="user.role === 'manager'"
            ></el-table-column> -->

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
            <!-- <el-table-column
              v-if="user.role === 'manager'"
              label="管理员操作"
              width="180"
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
            </el-table-column> -->
          </el-table>
        </el-card>
      </el-col>
    </el-row>

  </div>

  <!-- <el-card shadow="hover" style="height: 403px">
    <chart :chartData="this.chartData" />
  </el-card> -->
</template>

<script>
// Echarts Part BEGIN
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart } from "echarts/charts";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
} from "echarts/components";
import VChart, { THEME_KEY } from "vue-echarts";
import { ref, defineComponent } from "vue";

use([
  CanvasRenderer,
  PieChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
]);

import { getBasicStatic, getAllData } from "@/api/data";
export default defineComponent({
  name: "dashboard",
  components: {
    VChart,
  },
  provide: {
    [THEME_KEY]: "light",
  },
  setup: () => {
    const option = ref({
      // title: {
      //   text: "Traffic Sources",
      //   left: "center",
      // },
      tooltip: {
        trigger: "item",
        formatter: "{a} <br/>{b} : {c} ({d}%)",
      },
      legend: {
        orient: "vertical",
        left: "right",
        data: ["Online", "Offline", "Error"],
      },
      series: [
        {
          name: "Traffic Sources",
          type: "pie",
          radius: "55%",
          center: ["50%", "60%"],
          data: [
            { value: 1335, name: "Online" },
            { value: 310, name: "Offline" },
            { value: 234, name: "Error" },
            // { value: 135, name: "Video Ads" },
            // { value: 1548, name: "Search Engines" },
          ],
          emphasis: {
            itemStyle: {
              shadowBlur: 10,
              shadowOffsetX: 0,
              shadowColor: "rgba(0, 0, 0, 0.5)",
            },
          },
        },
      ],
    });

    return { option };
  },

  data() {
    return {
      // chartData: {
      //   expectedData: [100, 120, 161, 134, 105, 160, 165],
      //   actualData: [120, 82, 91, 154, 162, 140, 145],
      // },
      recentData: [
        {
          time: "2020-2-1 9:00:00",
          facID: "001",
          // wardID: "01005",
          location: "est",
          type: "normal", // normal / warning
          amount: "37.2",
          unit: "摄氏度", // 需要根据facID查找
        },
        {
          time: "2020-2-1 9:00:05",
          facID: "002",
          // wardID: "09001",
          location: "wst",
          type: "warning",
          amount: "38.9",
          unit: "摄氏度",
        },
      ],
      basic: {
        facNum: 0,
        dataNum: 0,
        patientNum: 0,
        wardNum: 0,
      },
      clock: {
        timer: null,
        nowDate: "2021-06-18",
        nowTime: "22:59:00",
      },
      user: {
        ID: localStorage.getItem("ls_userID"),
        name: localStorage.getItem("ls_userName"),
        role: localStorage.getItem("ls_userRole"),
        email: localStorage.getItem("ls_userEmail"),
      },

      todoList: [
        {
          title: "今天要修复100个bug",
          status: false,
        },
        {
          title: "今天要修复100个bug",
          status: false,
        },
        {
          title: "今天要写100行代码加几个bug吧",
          status: false,
        },
        {
          title: "今天要修复100个bug",
          status: false,
        },
        {
          title: "今天要修复100个bug",
          status: true,
        },
        {
          title: "今天要写100行代码加几个bug吧",
          status: true,
        },
      ],
      data: [
        {
          name: "2018/09/04",
          value: 1083,
        },
        {
          name: "2018/09/05",
          value: 941,
        },
        {
          name: "2018/09/06",
          value: 1139,
        },
        {
          name: "2018/09/07",
          value: 816,
        },
        {
          name: "2018/09/08",
          value: 327,
        },
        {
          name: "2018/09/09",
          value: 228,
        },
        {
          name: "2018/09/10",
          value: 1065,
        },
      ],
      data_option1: {
        type: "bar",
        title: {
          text: "最近一周各品类销售图",
        },
        xRorate: 25,
        labels: ["周一", "周二", "周三", "周四", "周五"],
        datasets: [
          {
            label: "家电",
            data: [234, 278, 270, 190, 230],
          },
          {
            label: "百货",
            data: [164, 178, 190, 135, 160],
          },
          {
            label: "食品",
            data: [144, 198, 150, 235, 120],
          },
        ],
      },
      data_option2: {
        type: "line",
        title: {
          text: "最近几个月各品类销售趋势图",
        },
        labels: ["6月", "7月", "8月", "9月", "10月"],
        datasets: [
          {
            label: "家电",
            data: [234, 278, 270, 190, 230],
          },
          {
            label: "百货",
            data: [164, 178, 150, 135, 160],
          },
          {
            label: "食品",
            data: [74, 118, 200, 235, 90],
          },
        ],
      },
    };
  },

  computed: {
    userRole() {
      return localStorage.getItem("ls_userRole");
    },
    nowDate() {
      return this.clock.nowDate;
    },
    nowTime() {
      return this.clock.nowTime;
    },
  },
  created() {
    // 每秒钟需要执行的函数
    this.clock.timer = setInterval(() => {
      this.refreshDateTime();
      // this.getBasicStatic_();
      console.log("timer在执行");
    }, 60000);
  },
  mounted() {
    this.refreshDateTime();
    this.getBasicStatic_();
    this.getDetailData();
  },
  beforeUnmount() {
    if (this.clock.timer) {
      clearInterval(this.clock.timer);
    }
  },
  methods: {
    getBasicStatic_() {
      getBasicStatic()
        .then((res) => {
          // console.log("---in getBasicStatic---");
          // console.log(res.data);
          this.basic = res.data;
        })
        .catch(() => {
          this.$message.error("getBasicStatic后端服务器超时");
        });
    },
    getDetailData() {
      const params = {
        limit: 20,
        sort: "recent",
      };
      getAllData(params)
        .then((res) => {
          // console.log("---in getAllData---");
          // console.log(res.data);
          this.recentData = res.data.list;
        })
        .catch((e) => {
          console.log(e);
          this.$message.error("getAllData后端服务器超时");
        });
    },
    checkDigit(i) {
      if (i < 10) i = "0" + i;
      return i;
    },
    refreshDateTime() {
      let icnow = new Date();
      this.clock.nowDate =
        icnow.getFullYear() +
        "-" +
        this.checkDigit(icnow.getMonth() + 1) +
        "-" +
        this.checkDigit(icnow.getDate());
      this.clock.nowTime =
        this.checkDigit(icnow.getHours()) +
        ":" +
        this.checkDigit(icnow.getMinutes());
      // + ':' + this.checkDigit(icnow.getSeconds())
    },
  },
});
</script>

<style scoped>

.line-chart {
  height: 400px;
}

.pie-chart {
  height: 400px;
}

.card {
  margin-bottom: 20px;
}

.el-row {
  margin-bottom: 20px;
}

.grid-content {
  display: flex;
  align-items: center;
  height: 100px;
}

.grid-cont-right {
  flex: 1;
  text-align: center;
  font-size: 14px;
  color: #999;
}

.grid-num {
  font-size: 30px;
  font-weight: bold;
}

.grid-con-icon {
  font-size: 50px;
  width: 100px;
  height: 100px;
  text-align: center;
  line-height: 100px;
  color: #fff;
}
/* icon-1的icon颜色和字体颜色 */
.grid-con .grid-con-icon {
  background: #3e86ec;
}

.grid-con .grid-num {
  color: #3e86ec;
}

.user-info {
  display: flex;
  align-items: center;
  padding-bottom: 20px;
  border-bottom: 2px solid #ccc;
  margin-bottom: 20px;
}

.user-avator {
  width: 120px;
  height: 120px;
  border-radius: 50%;
}

.user-info-cont {
  padding-left: 10px;
  flex: 1;
  font-size: 14px;
  color: #999;
}

.user-info-cont div:first-child {
  font-size: 20px;
  text-align: center;
  color: #222;
}

.time-div div:first-child {
  color: #999;
  text-align: center;
}
.exact-time {
  font-size: 50px;
  text-align: center;
}

.user-info-list {
  font-size: 14px;
  color: #999;
  line-height: 25px;
}

.user-info-list span {
  margin-left: 0px;
  float: right;
  /* align-items: right; */
}

.mgb20 {
  margin-top: 20px;
  margin-bottom: 20px;
}

.todo-item {
  font-size: 14px;
}

.todo-item-del {
  text-decoration: line-through;
  color: #999;
}
</style>
