console.clear()
const print = (inner) => console.log(inner)
const express = require("express")
const bodyParser = require("body-parser")
const mongoose = require("mongoose")

const cookieParser = require("cookie-parser");
const sessions = require('express-session');

const app = express()


app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
app.use(sessions({
    secret: "thisismysecrctekeyfhrgfgrfrty84fwir767",
    saveUninitialized:true,
    resave: false
}));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());

app.set('view engine', 'ejs');


url = "mongodb+srv://dineshj2299:dineshj2299@cluster0.asj5t.mongodb.net/"
mongoose.connect(url, {useNewUrlParser: true, useUnifiedTopology: true},console.log("DB connected"));
const accounts_model = require("./model")

let out = []
// accounts_model.ins






app.get("/admin", (req, res) => {
    accounts_model.find({},(err,data)=>{
        if (err) throw err
        res.render("admin", { accounts: data })
    })
})

// out.forEach

app.post("/admin", (req, res) => {
    form = req.body
    accounts_model.insertMany(form,(err,data)=>{
        if (err) throw err
        
        
        // print(data)
        res.redirect("admin")
    })

})





app.get("/", (req, res) => {
    res.render("index")
})
app.post("/", (req, res) => {
    form = req.body
    res.render("index", { name: form.name })
})



app.get("/language", (req, res) => {
    res.render("language")
})
app.get("/language/:type", (req, res) => {
    print(req.params.type)
    req.session.language = req.params.type
    res.redirect("/pin")
})



account = undefined

app.get("/pin", (req, res) => {
    res.render("pin")
})
app.post("/pin", (req, res) => {
    accounts_model.findOne({"pin":req.body.pin},(err,data)=>{
        if (err) throw err
        req.session.obj = data
        // print(data)
        res.redirect("dashboard")
    })
})



app.get("/dashboard", (req, res) => {
    // print(req.session.obj.name)
    // print(req.session)
    res.render("dashboard",{obj:req.session.obj})
})



let dashboard = require("./dashboard")
app.use("/dashboard",dashboard)







port = 5000
app.listen(port, () => console.log(`Application Port on ${port}`))






