<template>
  <el-card shadow="hover" style="height: 403px">
    <template #header>
      <div class="clearfix">
        <span>echarts初尝试</span>
      </div>
    </template>
    <chart :chartData="this.chartData"/>
    <!-- <div id="myChart" :style="{ width: '300px', height: '300px' }"></div> -->
  </el-card>
</template>

<script>
import Chart from "./template_line_chart";

let echarts = require("echarts/lib/echarts");
import { GridComponent } from "echarts/components";
echarts.use([GridComponent]);
export default {
  data() {
    return {
      chartData: {
        expectedData: [100, 120, 161, 134, 105, 160, 165],
        actualData: [120, 82, 91, 154, 162, 140, 145]
      },
    };
  },
  components: { Chart },
  mounted() {
    // this.initChart();
  },
  methods: {
    initChart() {
      let myChart = echarts.init(document.getElementById("myChart"));
      myChart.setOption({
        title: { text: "在Vue中使用echarts" },
        tooltip: {},
        xAxis: {
          data: ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
        },
        yAxis: {},
        series: [
          {
            name: "销量",
            type: "bar",
            data: [5, 20, 36, 10, 10, 20],
          },
        ],
      });
    },
  },
};
</script>