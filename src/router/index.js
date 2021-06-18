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
          title: '首页'
        },
        component: () => import(
          /* webpackChunkName: "dashboard" */
          "../views/Dashboard.vue")
      },
      {
        path: "/table",
        name: "basetable",
        meta: {
          title: '表格'
        },
        component: () => import(
          /* webpackChunkName: "table" */
          "../views/BaseTable.vue")
      },
      // for test
      {
        path: "/charts",
        name: "echarts-test",
        meta: {
          title: '表格'
        },
        component: () => import(
          /* webpackChunkName: "table" */
          "../views/test/EchartsTest.vue")
      },
      // {
      //   path: "/charts",
      //   name: "basecharts",
      //   meta: {
      //     title: '图表'
      //   },
      //   component: () => import(
      //     /* webpackChunkName: "charts" */
      //     "../views/BaseCharts.vue")
      // },
      {
        path: "/form",
        name: "baseform",
        meta: {
          title: '表单'
        },
        component: () => import(
          /* webpackChunkName: "form" */
          "../views/BaseForm.vue")
      },
      {
        path: "/tabs",
        name: "tabs",
        meta: {
          title: 'tab标签'
        },
        component: () => import(
          /* webpackChunkName: "tabs" */
          "../views/Tabs.vue")
      },
      // {
      //   path: "/donate",
      //   name: "donate",
      //   meta: {
      //     title: '鼓励作者'
      //   },
      //   component: () => import(
      //     /* webpackChunkName: "donate" */
      //     "../views/Donate.vue")
      // },
      {
        path: "/permission",
        name: "permission",
        meta: {
          title: '权限管理',
          permission: true
        },
        component: () => import(
          /* webpackChunkName: "permission" */
          "../views/Permission.vue")
      },
      // {
      //   path: "/i18n",
      //   name: "i18n",
      //   meta: {
      //     title: '国际化语言'
      //   },
      //   component: () => import(
      //     "../views/I18n.vue")
      // },
      {
        path: "/upload",
        name: "upload",
        meta: {
          title: '上传插件'
        },
        component: () => import(
          /* webpackChunkName: "upload" */
          "../views/Upload.vue")
      },
      {
        path: "/icon",
        name: "icon",
        meta: {
          title: '自定义图标'
        },
        component: () => import(
          /* webpackChunkName: "icon" */
          "../views/Icon.vue")
      },
      {
        path: '/404',
        name: '404',
        meta: {
          title: '找不到页面'
        },
        component: () => import(/* webpackChunkName: "404" */
          '../views/404.vue')
      },
      {
        path: '/403',
        name: '403',
        meta: {
          title: '没有权限'
        },
        component: () => import(/* webpackChunkName: "403" */
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
      /* webpackChunkName: "login" */
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
