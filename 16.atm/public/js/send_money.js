
let inner = sessionStorage.getItem("language");

let data = []
const push = (id, value) =>  data.push({id: id , value : value })

if (inner == "tamil") {
    push("title_GURU", "குருநானக் ஏடிஎம்" )
    push("account_number", "வங்கி கணக்கு எண்" )
    
    push("amount", "அனுப்பும் தொகை" )
    push("account", "பெறுநரின் கணக்கு எண்" )
    push("submit_btn", "சமர்ப்பிக்கவும்" )


}
if (inner == "hindi") {
    
    push("title_GURU", "गुरु नानक एटीएम")
    push("account_number", "बैंक खाता संख्या")

    push("amount", "राशि भेजना" )
    push("account", "प्राप्तकर्ता खाता संख्या" )
    push("submit_btn", "प्रस्तुत")
    
}



data.forEach((item)=>{
    document.getElementById(item.id).innerHTML = item.value;
})