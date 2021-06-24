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
        path: "/table",
        name: "basetable",
        meta: {
          title: '基础表格'
        },
        component: () => import(
          "../views/BaseTable.vue")
      },
      {
        path: "/echarts",
        name: "echarts-test",
        meta: {
          title: 'vue-echarts测试模块'
        },
        component: () => import(
          "../views/test/vue-echarts.vue")
      },

      // {
      //   path: "/charts",
      //   name: "basecharts",
      //   meta: {
      //     title: '图表'
      //   },
      //   component: () => import(
      //     "../views/BaseCharts.vue")
      // },
      {
        path: "/form",
        name: "baseform",
        meta: {
          title: '表单相关'
        },
        component: () => import(
          "../views/BaseForm.vue")
      },
      {
        path: "/tabs",
        name: "tabs",
        meta: {
          title: 'tab选项卡'
        },
        component: () => import(
          "../views/Tabs.vue")
      },
      {
        path: "/permission",
        name: "permission",
        meta: {
          title: '权限测试',
          permission: true
        },
        component: () => import(
          "../views/Permission.vue")
      },
      {
        path: "/upload",
        name: "upload",
        meta: {
          title: '文件上传'
        },
        component: () => import(
          "../views/Upload.vue")
      },
      {
        path: "/icon",
        name: "icon",
        meta: {
          title: '自定义图标'
        },
        component: () => import(
          "../views/Icon.vue")
      },
      {
        path: '/404',
        name: '404',
        meta: {
          title: '404页面'
        },
        component: () => import(
          '../views/404.vue')
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
  if (!userRole && (to.path !== '/login') && (to.path !== '/register')) {
    console.log("您还没有登录");
    next('/login');
  }
  else if (to.meta.permission) {
    // 如果是管理员权限则可进入，这里只是简单的模拟管理员权限而已
    userRole === 'manager'
      ? next()
      : next('/403');
  } else {
    next();
  }
});

export default router;
