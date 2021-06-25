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
            v-for="item in selectedMarker"
            :key="item.position"
            :options="item"
            icon="http://maps.google.com/mapfiles/ms/icons/orange-dot.png"
            @click="clickMarker(item.zIndex)"
          >
            <!-- <GMapInfoWindow
              :open="openedMarkerID === item.zIndex"
              >
              <div>I am in info window
              </div>
            </GMapInfoWindow> -->

          </Marker>
          <Polyline
            v-for="item in selectedPolyline"
            :key="item.facID"
            :options="item"
          />
        </GoogleMap>
      </div>

      <div class="data-table">
        <div class="control-box">
          <el-form
            :inline="true"
            :model="selectForm"
            class="search-form-inline"
          >
            <!-- <el-form-item>
              <el-input
                v-model="selectForm.startTime"
                placeholder="筛选开始时间"
                clearable
              ></el-input>
            </el-form-item>

            <el-form-item>
              <el-input
                v-model="selectForm.endTime"
                placeholder="筛选终止时间"
                clearable
              ></el-input>
            </el-form-item> -->

            <el-form-item>
              <el-input
                v-model="selectForm.facID"
                placeholder="筛选设备ID"
                clearable
              ></el-input>
            </el-form-item>

            <el-form-item>
              <el-button icon="el-icon-search" circle @click="handleSelect"></el-button>
            </el-form-item>

            <el-form-item style="float:right;">

          <el-switch
            v-model="showPolyline"
            active-text="显示轨迹线"
            inactive-text=""
          >
          </el-switch>

          <el-button
            style="margin: 0 20px 20px 10px"
            type="primary"
            icon="el-icon-lx-refresh"
            plain
            @click="handleResetSelecion()"
          >
            重置筛选
          </el-button>
            </el-form-item>

          </el-form>


        </div>

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
import { getAllData } from "@/api/data.js";

export default defineComponent({
  name: "map-test",
  components: {
    GoogleMap,
    Marker,
    Polyline,
    // GMapInfoWindow,
  },
  data() {
    return {
      showPolyline: false,
      openedMarkerID: 0,
      selectForm: {
        startTime: "",
        endTime: "",
        facID: "",
      },
      // selectFacID: "",
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
      ],
    };
  },
  setup() {
    const center = { lat: 40.689247, lng: -74.044502 };
    const markerOptions = getMarkerOptions();
    const polylineOptions = getPolylineOptions();
    return { center, markerOptions, polylineOptions };
  },
  created() {
    this.getOriginalData();
  },
  mounted() {},
  computed: {
    tableData() {
      return this.originalData.filter((item) => {
        return item.facID.includes(this.selectForm.facID);
      });
    },
    selectedMarker() {
      return this.markerOptions.filter((item) => {
        return item.facID.includes(this.selectForm.facID);
      });
    },
    selectedPolyline() {
      if(this.showPolyline)
        return this.polylineOptions.filter((item) => {
          return item.facID.includes(this.selectForm.facID);
        });
      else
        return [];
    },
  },
  methods: {
    clickMarker(zIndex) {
      // console.log("click marker");
      // console.log("operation1: select a facID");
      // console.log("operation2: revert the showPolyline");
      console.log(zIndex);
      this.openedMarkerID = zIndex;
      // console.log(arg[0].latLng.lat());
      // console.log(arg[0].latLng.lng());
      // this.showPolyline = !this.showPolyline;
      // if (this.selectFacID == "020") {
      //   this.selectFacID = "";
      //   this.showPolyline = false;
      // } else {
      //   this.selectFacID = "020";
      //   this.showPolyline = true;
      // }
    },
    handleResetSelecion() {
      this.showPolyline = false;
      this.selectForm = {
        startTime: "",
        endTime: "",
        facID: "",
      };
    },
    handleSelect() {
      console.log("select");
      console.log(this.selectForm);
    },
    getOriginalData() {
      const params = {
        limit: 100,
        sort: "recent",
        startTime: "",
        endTime: "",
      };
      getAllData(params)
        .then((res) => {
          // console.log("in getAllData api");
          // console.log(res.data);
          this.originalData = res.data.list;
        })
        .catch((e) => {
          console.log(e);
          this.$message.error("getAllData后端服务器超时");
        });
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
