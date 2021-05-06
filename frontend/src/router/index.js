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
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  }, {
    name: "ProblemOne",
    path: "problem-one",
    component: async () => await import("../views/ViewOne")
  },
  {
    name: "ProblemTwo",
    path: "problem-two",
    component: async () => await import("../views/ViewTwo")
  }, {
    name: "ProblemTree",
    path: "problem-tree",
    component: async () => await import("../views/ViewTree")
  }
];

const router = new VueRouter({
  routes,
  mode: "history"
});

export default router;
