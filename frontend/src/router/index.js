import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  {
    name: "ProblemOne",
    path: "/problem-one",
    component: async () => await import("../views/ViewOne")
  },
  {
    name: "ProblemTwo",
    path: "/problem-two",
    component: async () => await import("../views/ViewTwo")
  },
  {
    name: "ProblemTree",
    path: "/problem-tree",
    component: async () => await import("../views/ViewTree")
  },
  {
    path: "*",
    name: "ErrorPrincipal",
    component: () => import("@/pages/LayoutError"),
  }
];

const router = new VueRouter({
  routes,
  mode: "history"
});

export default router;
