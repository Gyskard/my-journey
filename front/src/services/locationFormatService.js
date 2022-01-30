let locationFormatService = {};

locationFormatService.install = function (Vue) {
    Vue.prototype.$locationFormat = function (location) {
        let result = location["name"]
        location = Object.assign({}, {
            "house_number_street": location["house_number_street"],
            "street_name": location["street_name"],
            "postal_code": location["postal_code"],
            "city": location["city"],
            "country": location["country"],
        })
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
