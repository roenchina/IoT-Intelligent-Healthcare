<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-lx-calendar"></i> 地图视图
        </el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <el-row :gutter="20">
      <el-col :span="24">
        <el-card class="echats-card" shadow="hover">
          <template #header>
            <div class="clearfix">
              <span>地图</span>
            </div>
          </template>

          <div class="line-chart" style="height: 400px">
            <v-chart
              :option="mapOption"
              :init-option="initOptions"
              ref="mapOption"
              theme="light"
              autoresize
              @zr:click="handleZrClick"
              @click="handleClick"
            />
          </div>
        </el-card>
      </el-col>
    </el-row>

    <div class="container">
      <baidu-map
        class="bm-view"
        :center="mapCenter"
        :zoom="mapZoom"
        @ready="handleReady"
        ak="xWqFenIrYQr5OW5OHgZKTBZSSHMlBb0Q"
      >
      </baidu-map>
    </div>

    <div class="container">
      <baidu-map
        class="bm-view"
        center="北京"
        @ready="handleReady"
        ak="xWqFenIrYQr5OW5OHgZKTBZSSHMlBb0Q"
      >
      </baidu-map>
    </div>
  </div>
</template>

<script>
// baidu map import
import BaiduMap from "vue-baidu-map/components/map/Map.vue";
// import { BmlMarkerClusterer } from "vue-baidu-map";
// echarts import
import VChart from "vue-echarts";
import { use, registerMap } from "echarts/core";

import { MapChart, ScatterChart, EffectScatterChart } from "echarts/charts";

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

import mapOption from "@/data/map";
import chinaMap from "@/data/china.json";
registerMap("china", chinaMap);

use([
  MapChart,

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
  name: "map-view",
  components: {
    VChart,
    BaiduMap,
    // BmlMarkerClusterer,
  },
  data() {
    return {
      // baidu map
      mapCenter: {
        lng: 0,
        lat: 0,
      },
      mapZoom: 3,
      // echarts map
      mapOption,
      initOptions: {
        renderer: "canvas",
      },
    };
  },
  created() {},
  methods: {
    // baidu map
    handleReady({ BMap, map }) {
      console.log("BMap ready");
      console.log(BMap, map);
      this.mapCenter.lng = 116.404;
      this.mapCenter.lat = 39.915;
      this.mapZoom = 15;
    },
    // echarts map
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
.bm-view {
  width: 100%;
  height: 300px;
}

.container {
  margin-bottom: 10px;
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
