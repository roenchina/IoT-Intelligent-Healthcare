<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-lx-calendar"></i> 数据查询
        </el-breadcrumb-item>
        <el-breadcrumb-item> 病房病床数据分析 </el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <el-card class="echats-card" shadow="hover">
      <div class="chart-div">
        <v-chart
          :option="lineOption"
          :init-option="initOptions"
          ref="lineOption"
          theme="light"
          autoresize
          @zr:click="handleZrClick"
          @click="handleClick"
        />
      </div>
    </el-card>
  </div>
</template>

<script>
import VChart from "vue-echarts";
import {
  use,
  // registerTheme,
} from "echarts/core";

import {
  BarChart,
  PieChart,
  LineChart,
  ScatterChart,
  EffectScatterChart,
} from "echarts/charts";
import {
  GridComponent,
  PolarComponent,
  GeoComponent,
  TooltipComponent,
  LegendComponent,
  TitleComponent,
  VisualMapComponent,
  DatasetComponent,
  ToolboxComponent,
  DataZoomComponent,
} from "echarts/components";
import { CanvasRenderer, SVGRenderer } from "echarts/renderers";

use([
  BarChart,
  PieChart,
  LineChart,

  ScatterChart,
  EffectScatterChart,

  GridComponent,
  PolarComponent,
  GeoComponent,
  TooltipComponent,
  LegendComponent,
  TitleComponent,
  VisualMapComponent,
  DatasetComponent,
  CanvasRenderer,
  SVGRenderer,
  ToolboxComponent,
  DataZoomComponent,
]);

export default {
  name: "data_detail",
  components: {
    VChart,
  },
  data() {
    return {
      initOptions: {
        renderer: "canvas",
      },
      lineOption: {
        title: {
          text: "你所在的病房 - 一周温湿度",
          subtext: "仅供测试",
        },
        tooltip: {
          trigger: "axis",
        },
        legend: {
          data: ["温度", "湿度"],
        },
        toolbox: {
          show: true,
          feature: {
            dataZoom: {
              yAxisIndex: "none",
            },
            dataView: { readOnly: false },
            magicType: { type: ["line", "bar"] },
            restore: {},
            saveAsImage: {},
          },
        },
        xAxis: {
          type: "category",
          boundaryGap: false,
          data: ["周一", "周二", "周三", "周四", "周五", "周六", "周日"],
        },
        yAxis: [
          {
            type: "value",
            name: "温度",
            axisLabel: {
              formatter: " {value} °C",
            },
          },
          {
            type: "value",
            name: "湿度",
            axisLabel: {
              formatter: "{value} %",
            },
          }
        ],
        series: [
          {
            name: "温度",
            type: "line",
            data: [10, 11, 13, 11, 12, 12, 9],
            yAxisIndex: '0',
          },
          {
            name: "湿度",
            type: "line",
            data: [30, 41, 39, 50, 76, 70, 50],
            yAxisIndex: '1',
          },
        ],
      },
    };
  },
  created() {},
  methods: {
    handleZrClick(...args) {
      console.log("click from zrender", ...args);
    },
    handleClick(...args) {
      console.log("click from echarts", ...args);
    },
  },
};
</script>

<style scoped>
.chart-div {
  height: 600px;
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
</style>
