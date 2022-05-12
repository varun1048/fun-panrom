from flask import Flask, redirect,render_template, request, url_for
from flask_pymongo import PyMongo
from bson import ObjectId
print(Flask)

app  =  Flask("__main__")

app.config["MONGO_URI"] = "mongodb+srv://varun:varun@cluster.eji5z.mongodb.net/Boss"
app.secret_key = b'_5#y2L"F4Q8z/n/xec]/'
db = PyMongo(app).db


@app.route("/",methods=['GET',"POST"])
def index():   
    if request.method == "POST":
        form = request.form 
        db['orders'].insert_one(dict(form))
    return render_template("index.html",prodects=db['prodects'].find({}))


@app.route("/admin")
def admin():    
    return render_template("admin.html",orders=db['orders'].find({}),prodects=db['prodects'].find({}))


@app.route("/admin/add_prodect",methods=['GET',"POST"])
def add_prodect():    
    if request.method == "POST":
        form = request.form 
        db['prodects'].insert_one(dict(form))
        return redirect(url_for("admin"))
    return render_template("add_prodect.html")



@app.route("/admin/prodect/<string:_id>",methods=['GET',"POST"])
def prodect(_id):    
    if request.method == "POST":
        form = request.form 

        # return redirect(url_for("admin"))
    
    return render_template("prodect.html",prodect=db['prodects'].find_one({"_id":ObjectId(_id)}))






if __name__ == "__main__":
    app.run()
    
    # ip = "192.168.1.2"
    # app.run(host=ip, port=5000, debug=True, threaded=False)