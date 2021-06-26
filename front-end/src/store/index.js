import { createStore } from 'vuex'

export default createStore({
  state: {
    ifCollapse: false,
    // showDataID: 0,
  },
  mutations: {
    // 侧边栏折叠
    handleCollapse(state, data) {
      state.ifCollapse = data;
    },
    // handleShowData(state, id){
    //   if(state.showDataID == id)
    //     state.showDataID = 0;
    //   else
    //     state.showDataID = id;
    // },
  },
  actions: {},
  modules: {}
})