
let inner = sessionStorage.getItem("language");

let data = []
const push = (id, value) =>  data.push({id: id , value : value })

if (inner == "tamil") {
    push("title_GURU", "குருநானக் ஏடிஎம்" )
    push("main_message", "உங்கள் ஏடிஎம் பின் எண்ணை உள்ளிடவும்" )
    push("submit_btn", "சமர்ப்பிக்கவும்" )
}
if (inner == "hindi") {
    
    push("title_GURU", "गुरु नानक एटीएम")
    push("main_message", "अपना एटीएम पिन नंबर दर्ज करें")
    push("submit_btn", "प्रस्तुत")

    
}



data.forEach((item)=>{
    document.getElementById(item.id).innerHTML = item.value;
})