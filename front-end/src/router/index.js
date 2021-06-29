import { createRouter, createWebHistory } from "vue-router";
import Home from "@/components/Home.vue";

const routes = [
  {
    path: '/',
    redirect: '/dashboard'
  },
  {
    path: "/",
    name: "Home",
    component: Home,
    children: [
      {
        path: "/dashboard",
        name: "dashboard",
        meta: {
          title: '系统首页'
        },
        component: () => import(
          "../views/dashboard/Dashboard.vue")
      },
      {
        path: "/facility",
        name: "facility",
        meta: {
          title: '设备管理'
        },
        component: () => import(
          "../views/facility/Facility.vue")
      },
      {
        path: "/data_overview",
        name: "data_overview",
        meta: {
          title: '数据一览'
        },
        component: () => import(
          "../views/data/Overview.vue")
      },
      {
        path: "/data_detail",
        name: "data_detail",
        meta: {
          title: '病房病床数据查询'
        },
        component: () => import(
          "../views/data/Detail.vue")
      },
      {
        path: "/map",
        name: "map",
        meta: {
          title: '地图视图'
        },
        component: () => import(
          "../views/map/Map.vue")
      },
      {
        path: '/403',
        name: '403',
        meta: {
          title: '403页面'
        },
        component: () => import(
          '../views/403.vue')
      }
    ]
  },
  {
    path: "/login",
    name: "Login",
    meta: {
      title: '请登录'
    },
    component: () => import(
      "../views/user/Login.vue")
  },
  {
    path: "/register",
    name: "Register",
    meta: {
      title: '注册新账号'
    },
    component: () => import(
      "../views/user/Register.vue")
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

router.beforeEach((to, from, next) => {
  document.title = `${to.meta.title} | 智慧医疗物联网管理系统`;
  const userRole = localStorage.getItem('ls_userRole');
  // console.log(userRole);
  if (!userRole && (to.path !== '/login') && (to.path !== '/register')) {
    console.log("检测到未登录");
    next('/login');
  }
  else if (to.path === '/facility' || to.path === '/data_overview' || to.path === '/map') {
    // 病人无法查看的页面
    userRole === 'patient'
      ? next('/403')
      : next();
  } else {
    next();
  }
});

export default router;
