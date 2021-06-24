<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-lx-calendar"></i> 地图视图
        </el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <!-- <div class="container">
      <baidu-map
        class="bm-view"
        :center="mapCenter"
        :zoom="mapZoom"
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
    </div> -->

    <!-- <div class="container">
      <baidu-map
        class="bm-view"
        :center="北京"
        @ready="handleReady"
        ak="xWqFenIrYQr5OW5OHgZKTBZSSHMlBb0Q"
      >
      </baidu-map>
    </div> -->
    <GoogleMap
      api-key="AIzaSyBHyiVWRgD6L3Zvgn7dFGL0N5ytYVaJmWM"
      style="width: 100%; height: 500px"
      :center="center"
      :zoom="15"
    >
      <Marker :options="{ position: center }" />
    </GoogleMap>
  </div>
</template>

<script>
// baidu map import
// import BaiduMap from "vue-baidu-map/components/map/Map.vue";
// import { BmlMarkerClusterer } from "vue-baidu-map";
import { defineComponent } from "vue";
import { GoogleMap, Marker } from "vue3-google-map";
export default defineComponent({
  name: "map-view",
  components: {
    // BaiduMap,
    GoogleMap,
    Marker,
    // BmlMarkerClusterer,
  },
  data() {
    return {
      // baidu map
      center : { lat: 40.689247, lng: -74.044502 },
      mapCenter: {
        lng: 116.404,
        lat: 39.915,
      },
      mapZoom: 15,
    };
  },
  created() {},
  mounted() {},
  methods: {
    setup() {
      const center = { lat: 40.689247, lng: -74.044502 };
      return { center };
    },
    // baidu map
    handleReady({ BMap, map }) {
      console.log("BMap ready");
      console.log(BMap, map);
      this.mapCenter.lng = 116.404;
      this.mapCenter.lat = 39.915;
      this.mapZoom = 15;
    },
  },
});
</script>

<style scoped>
.bm-view {
  width: 100%;
  height: 300px;
}

.container {
  margin-bottom: 10px;
  width: 100%;
  height: 300px;
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
