<template>
  <el-card shadow="hover" style="height: 403px">
    <chart :chartData="this.chartData" />
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
        actualData: [120, 82, 91, 154, 162, 140, 145],
      },
    };
  },
  components: { Chart },
  mounted() {},
  methods: {},
};
</script>