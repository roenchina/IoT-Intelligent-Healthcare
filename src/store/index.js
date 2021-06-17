import { createStore } from 'vuex'

export default createStore({
  state: {
    ifCollapse: false
  },
  mutations: {
    // 侧边栏折叠
    handleCollapse(state, data) {
      state.ifCollapse = data;
    }
  },
  actions: {},
  modules: {}
})