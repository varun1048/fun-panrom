const print = (inner) => console.log(inner)

const express = require("express")
const accounts_model = require("./model")
let router = express.Router()


const current_data = () => {

    var currentdate = new Date();
    return currentdate.getDate() + "/"
        + (currentdate.getMonth() + 1) + "/"
        + currentdate.getFullYear() + " @ "
        + currentdate.getHours() + ":"
        + currentdate.getMinutes() + ":"
        + currentdate.getSeconds();

}
// mini_statement
router.get("/balance_inquiry", (req, res) => {

    accounts_model.findOne({ "pin": req.session.obj.pin }, (err, data) => {
        if (err) throw err
        // req.session.destroy((err)=> {if(err)throw err})
        req.session.obj = data
        res.render("dashboard/balance_inquiry", {
            obj: req.session.obj,
            current_data: current_data()
        })
    })
})








router.get("/withdrawal", (req, res) => {


    res.render("dashboard/withdrawal", {
        obj: req.session.obj,
    })
})



router.post("/withdrawal", (req, res) => {
    let withdraw_amount = req.body.withdraw_amount
    // print(withdraw_amount)

    accounts_model.findOne({ "pin": req.session.obj.pin }, (err, data) => {
        if (err) throw err

        // if ( withdraw_amount % 5 == 0) {
        //     str = "It should be divisible by 5"
        //     res.redirect(`transaction/${str}/0`)
        // }
        if (withdraw_amount < 100) {
            str = "Menimum amount of  transaction 100 Rs"
            res.redirect(`transaction/${str}/0`)
        }
        else {

            if (withdraw_amount < data.amount) {

                let transaction = [{ type: "Debit", amount: withdraw_amount, current_data: current_data() }].concat(data.transaction)
                const filter = { pin: req.session.obj.pin };
                const update = { "$inc": { amount: - withdraw_amount }, "$set": { transaction: transaction } };

                accounts_model.findOneAndUpdate(filter, update, (err, data) => {
                    if (err) throw err
                    // print(data)
                    req.session.obj = data
                    str = "Transaction successfull, Please  collect your cash."
                    res.redirect(`transaction/${str}/1`)
                })

            }

            else {
                res.redirect("transaction/Insufficient Balance/0")
            }
        }
    })

    // res.redirect("/dashboard/balance_inquiry")
})





router.get("/deposit", (req, res) => {
    res.render("dashboard/deposit", { obj: req.session.obj, })
})


router.post("/deposit", (req, res) => {
    let deposit_amount = req.body.deposit_amount


    accounts_model.findOne({ "pin": req.session.obj.pin }, (err, data) => {
        if (err) throw err

        let transaction = [{ type: "Credit", amount: deposit_amount, current_data: current_data() }].concat(data.transaction)
        const filter = { pin: req.session.obj.pin };
        const update = { "$inc": { amount: deposit_amount }, "$set": { transaction: transaction } };

        accounts_model.findOneAndUpdate(filter, update, (err, data) => {
            if (err) throw err
            // print(data)
            req.session.obj = data
            str = "Transaction successfull."
            res.redirect(`transaction/${str}/1`)
        })


    })

    // res.redirect("/dashboard/balance_inquiry")
})



router.get("/mini_statement", (req, res) => {

    accounts_model.findOne({ "pin": req.session.obj.pin }, (err, data) => {
        if (err) throw err
        req.session.obj = data
        res.render("dashboard/mini_statement", { obj: req.session.obj })

    })
})



router.get("/change_pin", (req, res) => res.render("dashboard/change_pin",{ obj: req.session.obj, }))
router.post("/change_pin", (req, res) => {
    form = req.body
    if (form.pin1 == form.pin1) {

        const filter = { pin: req.session.obj.pin };
        const update = { "$set": { pin: form.pin1 } };


        accounts_model.findOneAndUpdate(filter, update, (err, data) => {
            if (err) throw err
            res.redirect("/pin")
        })
    }
    else {
        let str = "Both pin number not matched.."
        res.redirect(`transaction/${str}/0`)
    }
})




router.get("/send_money", (req, res) => res.render("dashboard/send_money",{ obj: req.session.obj, }))
router.post("/send_money", (req, res) => {
    sending_amount = req.body.amount
    account = req.body.account

    accounts_model.findOne({ "account": account }, (err, Receiver) => {
        if (err) throw err
        try {
            print("Sender name " + Receiver.name  )






            accounts_model.findOne({ "pin": req.session.obj.pin }, (err, main) => {
                // accounts_model.findOne({ "pin": "1" }, (err, data) => {
                if (err) throw err
                if (sending_amount < main.amount) {
                    // res.send(data)

                    let transaction = [{ type: "Transferd - D", amount: sending_amount, current_data: current_data() }].concat(main.transaction)
                    const filter = { pin: req.session.obj.pin };
                    const update = { "$inc": { amount: - sending_amount }, "$set": { transaction: transaction } };
                    accounts_model.findOneAndUpdate(filter, update, (err, data2) => {
                        if (err) throw err
                    // str = "Transaction successfull, To the account " + account
                        // res.redirect(`transaction/${str}/1`)
                    })




                    

                        //Receiver
                        let Received_transaction = [{ type: "Received - C", amount: sending_amount, current_data: current_data() }].concat(Receiver.transaction)
                        const Received_filter = { "account": Receiver.account };
                        const Received_update = { "$inc": { amount:  sending_amount }, "$set": { transaction: Received_transaction } };
                        accounts_model.findOneAndUpdate(Received_filter, Received_update, (err, Received2) => {
                            if (err) throw err

                           print("-------------"+Received2.name)
                            
                        })

                        str = "Transaction successfull, To the account " + account
                        res.redirect(`transaction/${str}/1`)


                }
                else {
                    res.redirect("transaction/Insufficient Balance/0")
                }
            })











        }
        catch (err) {
            
            res.redirect("transaction/Receiver  account invalied/0")
        }
    })




    // accounts_model.findOne({ "account": account }, (err, data) => {
    //     if (err) throw err
    //     res.send(data)
    // })
})






router.get("/transaction/:transaction/:result", (req, res) => {

    res.render("dashboard/transaction", {
        message: req.params.transaction,
        result: Boolean(Number(req.params.result)),
        obj: req.session.obj,
    })
})





module.exports = router