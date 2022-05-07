const mongoose = require("mongoose")
let schema = new mongoose.Schema({
    name: { type: String, required: true },
    account: { type: String, required: true },
    pin: { type: String, required: true },

    amount: { type: Number, required: false,default: 0 },
})
module.exports = mongoose.model("accounts",schema)

