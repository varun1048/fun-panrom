# env\Scripts\activate
import random  
from bson import ObjectId
from flask import Flask, redirect,render_template, request, url_for
from flask_pymongo import PyMongo

app  =  Flask("__main__")

app.config["MONGO_URI"] = "mongodb+srv://saravanamuthusha:Register@cluster0.azsub.mongodb.net/vels"
app.secret_key = b'_5#y2L"F4Q8z/n/xec]/'
db = PyMongo(app).db



@app.route("/",methods=['GET',"POST"])
def index():    
    if request.method == "POST":
        form = request.form
        result = db['students'].find_one({"roll_number":form['roll_name']})
        print(result)
        return redirect(url_for("student",_id=result['_id']))
        
        
    return render_template("student/home.html")


@app.route("/student/<string:_id>",methods=['GET',"POST"])
def student(_id):
    student = db['students'].find_one({"_id":ObjectId(_id)})
    questions = list(db['aptitude'].find({}))
    
    
    
    if request.method == "POST":
        form = request.form
        
        

        # print(stu)
        for x in range(0, len(questions)):
            obj = (form[str(x)]).split("____") 
            question = db['aptitude'].find_one({"_id":ObjectId(obj[1])})
            # print(question)
            if question['answer'] == obj[0]:
                
                db['students'].find_one_and_update(
                    {"_id":ObjectId(  form['_id'])},
                    {"$inc":{"mark":1}}
                )
        
        db['students'].find_one_and_update(
                    {"_id":ObjectId(  form['_id'])},
                    {"$set":{"test":True}}
                )
        return redirect(url_for("student/students",_id=form['_id']))
    
    
    if student['test']:
        return render_template("student/result.html", student = student)
    
    
    for x in questions:
        random.shuffle(x['options'])    
        
    random.shuffle(questions)
    return render_template("student.html", questions= enumerate(questions) , student = student)











@app.route("/admin")
def admin():
    students = list(db['students'].find({}))
    aptitude = list(db['aptitude'].find({}))
    return render_template("admin/home.html"    ,page="home" ,students=len(students),questions=len(aptitude))


@app.route("/live")
def live():  
    students_list = list( db['students'].find({}) )
    return render_template("admin/live.html"    ,page="live" ,students_list=students_list)


@app.route("/aptitude",methods=['GET',"POST"])
def aptitude():
    if request.method == "POST":
        form = request.form
        db['aptitude'].insert_one({
            
            "question":form['question'],
            "answer":form['answer'],
            "options":[form['option1'],form['option2'] , form['answer']],
        })
        return redirect(url_for("aptitude"))
    
    aptitude = list(db['aptitude'].find({}))
    return render_template("admin/aptitude.html"    ,page="aptitude", aptitude=aptitude[::-1])


@app.route("/add_student",methods=['GET',"POST"])
def add_student():
    if request.method == "POST":
        form = request.form
            
        db['students'].insert_one({
            "name":form['name'],
            "roll_number":form['roll_number'],
            "mark":0,
            "test":False,
        })
        return redirect(url_for("student_list"))        
    
    students_list = list( db['students'].find({}) )
    return render_template("admin/add_student.html" ,page="add_student" , students_list = students_list[::-1])









if __name__ == "__main__":
    # app.run()
    
    ip = "192.168.1.2"
    app.run(host=ip, port=5000, debug=True, threaded=False)