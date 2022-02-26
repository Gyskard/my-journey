import axios from "axios";

let httpService = {};
let http = axios;

http.defaults.baseURL = "http://localhost:8000"

http.interceptors.response.use(
    response => response.data,
    function (error) {
        console.log(error)
        return Promise.reject(error);
    }
);

httpService.install = function (Vue) {
    Vue.prototype.$http = http;
};

export default httpService;
