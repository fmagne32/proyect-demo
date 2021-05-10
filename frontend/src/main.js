import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';
import Vuelidate from 'vuelidate'

Vue.config.productionTip = false;
Vue.use(VueSweetalert2);
Vue.use(VueAxios, axios)
Vue.use(Vuelidate)
axios.defaults.baseURL = "http://localhost:8000/api/";

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
