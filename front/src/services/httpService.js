import axios from "axios";

let httpService = {};
let http = axios;

http.defaults.baseURL = "http://localhost:8000"

httpService.install = function (Vue) {
    Vue.prototype.$http = http;
};

export default httpService;
