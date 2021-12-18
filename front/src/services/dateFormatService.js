let dateFormatService = {};

dateFormatService.install = function (Vue) {
    Vue.prototype.$dateFormat = function (date) {
        const [year, month, day] = date.split('-')
        return `${day}/${month}/${year}`
    };
};

export default dateFormatService;
