
let inner = sessionStorage.getItem("language");

let data = []
const push = (id, value) =>  data.push({id: id , value : value })

if (inner == "tamil") {
    push("title_GURU", "குருநானக் ஏடிஎம்" )
    push("account_number", "வங்கி கணக்கு எண்" )

    push("withdraw_message", "பெறும் தொகை" )
    push("withdraw_btn", "சமர்ப்பிக்கவும்" )
}
if (inner == "hindi") {
    
    push("title_GURU", "गुरु नानक एटीएम")
    push("account_number", "बैंक खाता संख्या")

    push("withdraw_message", "प्रीटेकिंग राशि")
    push("withdraw_btn", "लेना")

    
}



data.forEach((item)=>{
    document.getElementById(item.id).innerHTML = item.value;
})