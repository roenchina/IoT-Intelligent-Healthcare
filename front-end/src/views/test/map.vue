<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-lx-calendar"></i> 地图视图
        </el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <div class="container">
      <div class="google-map">
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
          <Polyline v-if="showPolyline" :options="flightPath" />
        </GoogleMap>
      </div>

      <div class="data-table">
        <el-button
          style="margin: 0 20px 20px 0"
          type="primary"
          icon="el-icon-document"
          plain
          @click="handleResetSelecion()"
        >
          重置
        </el-button>
        <el-table
          :data="tableData"
          ref="tableData"
          border
          class="table"
          header-cell-class-name="table-header"
          :default-sort="{ prop: 'time', order: 'descending' }"
        >
          <el-table-column
            prop="facID"
            label="设备号"
            align="center"
            sortable
          ></el-table-column>

          <el-table-column
            prop="_ID"
            label="数据ID"
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
        </el-table>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { GoogleMap, Marker, Polyline } from "vue3-google-map";
import getMarkerOptions from "@/data/markerOptions";
import getPolylineOptions from "@/data/polylineOptions";

export default defineComponent({
  name: "map-test",
  components: {
    GoogleMap,
    Marker,
    Polyline,
  },
  data() {
    return {
      showPolyline: false,
      selectFacID: "",
      originalData: [
        {
          _ID: "10001",
          facID: "5211",
          time: "2021-6-23",
          location: "est",
          type: "normal", // normal / warning
          amount: "37.2",
          unit: "摄氏度", // 需要根据facID查找
          facType: "体温",
        },
        {
          _ID: "10008",
          facID: "1002",
          time: "2020-2-1",
          location: "wst",
          type: "warning",
          amount: "38.9",
          unit: "摄氏度",
          facType: "体温",
        },
      ],
    };
  },
  setup() {
    const center = { lat: 40.689247, lng: -74.044502 };
    const markerOptions = getMarkerOptions();
    const flightPath = getPolylineOptions();
    return { center, markerOptions, flightPath };
  },
  created() {},
  mounted() {},
  computed: {
    tableData() {
      return this.originalData.filter((item) => {
        return(
          item.facID.includes(this.selectFacID)
        );
      });
    },
  },
  methods: {
    clickMarker(...arg) {
      console.log("click marker");
      console.log("operation1: select a facID");
      console.log("operation2: revert the showPolyline");
      console.log(arg);
      // console.log(arg[0].latLng.lat());
      // console.log(arg[0].latLng.lng());
      this.showPolyline = !this.showPolyline;
      if(this.selectFacID == "1002") {
        this.selectFacID = "";
        this.showPolyline = false;
      }
      else {
        this.selectFacID = "1002";
        this.showPolyline = true;
      }
    },
    handleResetSelecion() {
      this.showPolyline = false;
      this.selectFacID = "";
    },
  },
});
</script>

<style scoped>
/* .container {
  margin-bottom: 10px;
  width: 100%;
  height: 300px;
} */
.data-table {
  margin-top: 20px;
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
