<template>
  <div class="about">
    <v-header />
    <v-sidebar />
    <div class="content-box" :class="{ 'content-collapse': ifCollapse }">
      <div class="content">
        <router-view v-slot="{ Component }">
          <transition name="move" mode="out-in">
            <component :is="Component" />
          </transition>
        </router-view>
      </div>
    </div>
  </div>
</template>
<script>
import vHeader from "./Header";
import vSidebar from "./Sidebar";
export default {
  components: {
    vHeader,
    vSidebar,
  },
  computed: {
    ifCollapse() {
      return this.$store.state.ifCollapse;
    },
  },
};
</script>
