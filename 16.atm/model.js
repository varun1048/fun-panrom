const mongoose = require("mongoose")
const current_data = () => {

    var currentdate = new Date();
    return currentdate.getDate() + "/"
        + (currentdate.getMonth() + 1) + "/"
        + currentdate.getFullYear() + " @ "
        + currentdate.getHours() + ":"
        + currentdate.getMinutes() + ":"
        + currentdate.getSeconds();

}
let schema = new mongoose.Schema({
    name: { type: String, required: true },
    account: { type: String, required: true },
    pin: { type: String, required: true },

    amount: { type: Number, required: false,default: 500 },
    transaction: { type: Array, required: false,default: [{ type: "Opening - D", amount: 500, current_data: current_data() }] },
})
module.exports = mongoose.model("accounts",schema)


