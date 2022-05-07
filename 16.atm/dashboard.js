const print = (inner) => console.log(inner)

const express = require("express")
const accounts_model = require("./model")
let router = express.Router()


const current_data = ()=>{

    var currentdate = new Date(); 
    return "as of " + currentdate.getDate() + "/"
    + (currentdate.getMonth()+1)  + "/" 
    + currentdate.getFullYear() + " @ "  
    + currentdate.getHours() + ":"  
    + currentdate.getMinutes() + ":" 
    + currentdate.getSeconds();
    
}

router.get("/balance_inquiry",(req,res)=>{
    
    accounts_model.findOne({"pin":req.session.obj.pin},(err,data)=>{
        if (err) throw err
        // req.session.destroy((err)=> {if(err)throw err})
        req.session.obj = data
        res.render("dashboard/balance_inquiry",{
            obj:req.session.obj,
            current_data:current_data()
        })
    })
})



router.get("/withdrawal",(req,res)=>{
    
    accounts_model.findOne({"pin":req.session.obj.pin},(err,data)=>{
        if (err) throw err
        // req.session.destroy((err)=> {if(err)throw err})
        req.session.obj = data
        res.render("dashboard/withdrawal",{
            obj:req.session.obj,
        })
    })
})



router.post("/withdrawal",(req,res)=>{
    let withdraw_amount = req.body.withdraw_amount
    // print(withdraw_amount)
    

    const filter = { pin: req.session.obj.pin };
    const update = { "$inc" :{amount: - withdraw_amount} };
    accounts_model.findOneAndUpdate(filter,update,(err,data)=>{
        if (err) throw err
        // req.session.destroy((err)=> {if(err)throw err})
        print(data)
        req.session.obj = data

    })
    res.redirect("/dashboard/balance_inquiry")
})


module.exports =  router