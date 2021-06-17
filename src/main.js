import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementPlus from 'element-plus'
import 'element-plus/lib/theme-chalk/index.css'
import './assets/css/icon.css'
const app = createApp(App)
// import installElementPlus from './plugins/element'
// installElementPlus(app)
app
  .use(ElementPlus)
  .use(store)
  .use(router)
  .mount('#app')