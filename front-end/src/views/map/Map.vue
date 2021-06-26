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
        <GMapMap
          api-key="AIzaSyBHyiVWRgD6L3Zvgn7dFGL0N5ytYVaJmWM"
          style="width: 100%; height: 500px"
          :center="mapCenter"
          :zoom="14"
        >
          <GMapMarker
            v-for="item in selectedMarker"
            :key="item.position"
            :options="item"
            @click="clickMarker(item.zIndex)"
          >
            <GMapInfoWindow :opened="openedMarkerID === item.zIndex">
              <div> {{ item.info }}</div>
            </GMapInfoWindow>
          </GMapMarker>
          <GMapPolyline
            v-for="item in selectedPolyline"
            :key="item.facID"
            :options="item"
          />
        </GMapMap>
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
              <el-button
                icon="el-icon-search"
                circle
                @click="handleSelect"
                disabled
              ></el-button>
            </el-form-item>

            <el-form-item style="float: right">
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

// <script>
import { getAllData } from "@/api/data.js";
import { getAllMarkers, getAllPolyline} from "@/api/charts.js";

export default {
  name: "map-test",
  components: {},
  data() {
    return {
      showPolyline: false,
      openedMarkerID: -1,
      mapCenter: { lat: 40.689247, lng: -74.044502 },
      selectForm: {
        startTime: "",
        endTime: "",
        facID: "",
      },
      originalMarker: [],
      originalPolyline: [],
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
  created() {
    this.getOriginalData();
    this.getMarkerOptions();
    this.getPolylineOptions();
  },
  mounted() {},
  computed: {
    tableData() {
      return this.originalData.filter((item) => {
        return item.facID.includes(this.selectForm.facID);
      });
    },
    selectedMarker() {
      return this.originalMarker.filter((item) => {
        return item.facID.includes(this.selectForm.facID);
      });
    },
    selectedPolyline() {
      if (this.showPolyline)
        return this.originalPolyline.filter((item) => {
          return item.facID.includes(this.selectForm.facID);
        });
      else return [];
    },
  },
  methods: {
    clickMarker(zIndex) {
      this.openedMarkerID = zIndex;
      // console.log(zIndex);
      // console.log(this.openedMarkerID);
    },
    handleResetSelecion() {
      this.showPolyline = false;
      this.openedMarkerID = -1;
      this.selectForm = {
        startTime: "",
        endTime: "",
        facID: "",
      };
    },
    handleSelect() {
      // console.log("select");
      // console.log(this.selectForm);
    },
    getMarkerOptions() {
      getAllMarkers()
        .then((res) =>{
          this.originalMarker = res.data.list;
        })
        .catch((e) => {
          console.log(e);
          this.$message.error("getAllMarkers后端服务器超时");
        })
    },
    getPolylineOptions() {
      getAllPolyline()
        .then((res) =>{
          this.originalPolyline = res.data.list;
        })
        .catch((e) => {
          console.log(e);
          this.$message.error("getAllPolyline后端服务器超时");
        })
    },
    getOriginalData() {
      const params = {
        limit: 100,
        sort: "recent",
        // startTime: "",
        // endTime: "",
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
};
</script>

<style scoped>
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
