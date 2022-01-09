import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import axios from "axios";
import dateFormatService from "./services/dateFormatService"
import locationFormatService from "@/services/locationFormatService";

Vue.config.productionTip = false

Vue.use(dateFormatService)
Vue.use(locationFormatService)

Vue.prototype.$api = 'http://localhost:8000'
Vue.prototype.$http = axios

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
