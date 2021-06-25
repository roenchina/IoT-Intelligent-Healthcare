<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-lx-calendar"></i> 地图视图
        </el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <GoogleMap
      api-key="AIzaSyBHyiVWRgD6L3Zvgn7dFGL0N5ytYVaJmWM"
      style="width: 100%; height: 500px"
      :center="center"
      :zoom="15"
    >
      <!-- <Marker :options="markerOptions" @click="clickMarker" /> -->
      <Marker
        v-for="item in markerOptions"
        :key="item.label"
        :options="item"
        icon="http://maps.google.com/mapfiles/ms/icons/orange-dot.png"
        @click="clickMarker"
      />
    </GoogleMap>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { GoogleMap, Marker } from "vue3-google-map";
import getMarkerOptions from "@/data/markerOptions";

export default defineComponent({
  name: "map-test",
  components: {
    GoogleMap,
    Marker,
  },
  data() {
    return {
      
    };
  },
  setup() {
    const center = { lat: 40.689247, lng: -74.044502 };
    const markerOptions = getMarkerOptions();
    // console.log(markerOptions);

    return { center, markerOptions };
  },
  created() {},
  mounted() {},
  methods: {
    clickMarker(...arg) {
      console.log("click marker");
      console.log(arg);
      console.log(arg[0].latLng.lat());
      console.log(arg[0].latLng.lng());
    },
  },
});
</script>

<style scoped>
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
