import { createApp } from 'vue'
import App from '@/App.vue'
import router from '@/router'
import store from '@/store'
import axios from 'axios'
import ElementPlus from 'element-plus'

// echarts
// import Echarts from 'vue-echarts'
// import {use} from 'echarts/core'

// import {
//   CanvasRenderer
// } from 'echarts/renderers'
// import {
//   BarChart
// } from 'echarts/charts'
// import {
//   GridComponent,
//   TooltipComponent
// } from 'echarts/components'

// use([
//   CanvasRenderer,
//   BarChart,
//   GridComponent,
//   TooltipComponent
// ]);

// element-ui
import 'element-plus/lib/theme-chalk/index.css'
import '@/assets/css/icon.css'

const app = createApp(App)
// installElementPlus(app)
app.config.globalProperties.$axios = axios
app.use(store)
   .use(router)
   .use(ElementPlus)
  //  .component('v-charts', Echarts)
   .mount('#app')