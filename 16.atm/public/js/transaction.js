
let inner = sessionStorage.getItem("language");

let data = []
const push = (id, value) =>  data.push({id: id , value : value })

if (inner == "tamil") {
    push("title_GURU", "குருநானக் ஏடிஎம்" )
    
    push("account_number", "வங்கி கணக்கு எண்" )
    push("submit_btn", "முதன்மை பட்டியல்" )
}
if (inner == "hindi") {
    
    push("title_GURU", "गुरु नानक एटीएम")

    push("account_number", "बैंक खाता संख्या")
    push("submit_btn", "मुख्य मेन्यू")

    
}



data.forEach((item)=>{
    document.getElementById(item.id).innerHTML = item.value;
})