
let inner = sessionStorage.getItem("language");

let data = []
const push = (id, value) =>  data.push({id: id , value : value })

if (inner == "tamil") {
    push("title_GURU", "குருநானக் ஏடிஎம்" )

    push("account_number", "வங்கி கணக்கு எண்" )
    push("withdrawal", "பணம் எடுக்க" )
    push("deposit", "பணம் போடுதல்" )
    push("balance", "இருப்பு" )
    push("mini_statement", "சிறு அறிக்கை" )
    push("send_money", "பணம் அனுப்ப" )
    push("change_pin", "வங்கி பின் எண்ணை மாற்ற" )
}
if (inner == "hindi") {
    
    push("title_GURU", "गुरु नानक एटीएम")
    push("account_number", "बैंक खाता संख्या")
    
    push("withdrawal", "पैसे का सौदा")
    push("deposit", "पैसा लगाना" )
    push("balance", "धन संतुलन" )
    push("mini_statement", "मिनी स्टेटमेंट" )
    push("send_money", "पैसे भेजना" )
    push("change_pin", "बैंक पिन नंबर बदलने के लिए" )

    

    
}



data.forEach((item)=>{
    document.getElementById(item.id).innerHTML = item.value;
})