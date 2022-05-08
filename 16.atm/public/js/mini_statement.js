
let inner = sessionStorage.getItem("language");

let data = []
const push = (id, value) =>  data.push({id: id , value : value })

if (inner == "tamil") {
    push("title_GURU", "குருநானக் ஏடிஎம்" )
    push("account_number", "வங்கி கணக்கு எண்" )

    push("main_menu", "முதன்மை பட்டியல்" )

    push("transaction", "பரிவர்த்தனை" )
    push("amount", "தொகை" )
    push("date", "தேதி மற்றும் நேரம்" )


}
if (inner == "hindi") {
    
    push("title_GURU", "गुरु नानक एटीएम")
    push("account_number", "बैंक खाता संख्या")

    push("main_menu", "मुख्य मेन्यू" )

    push("transaction", "लेन-देन" )
    push("amount", "रकम" )
    push("date", "दिनांक और समय" )
}



data.forEach((item)=>{
    document.getElementById(item.id).innerHTML = item.value;
})