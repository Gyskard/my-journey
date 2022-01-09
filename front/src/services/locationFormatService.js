let locationFormatService = {};

locationFormatService.install = function (Vue) {
    Vue.prototype.$locationFormat = function (location) {
        let result = location["name"]
        delete location["name"]
        delete location["id"]
        console.log(location)
        if (Object.values(location).some(elm => elm !== null)) {
            result += " ("
            for (const elm of ["house_number_street", "street_name", "postal_code", "city", "country"]) {
                result += `${location[elm] !== null ? location[elm] + ", " : ""}`
            }
            result = result.slice(0,-2) + ")"
        }
        return result
    };
};

export default locationFormatService;
