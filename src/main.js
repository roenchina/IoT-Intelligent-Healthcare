import { createApp } from 'vue'
import App from '@/App.vue'
import router from '@/router'
import store from '@/store'
import axios from 'axios'
import ElementPlus from 'element-plus'

// element-ui
import 'element-plus/lib/theme-chalk/index.css'
import '@/assets/css/icon.css'

// googleMap
import VueGoogleMaps from '@fawmi/vue-google-maps'

const app = createApp(App)
// installElementPlus(app)
app.config.globalProperties.$axios = axios
app.use(store)
   .use(router)
   .use(ElementPlus)
   .use(VueGoogleMaps, {
      load: {
         key: 'AIzaSyBHyiVWRgD6L3Zvgn7dFGL0N5ytYVaJmWM',
      },
   })
   .mount('#app')