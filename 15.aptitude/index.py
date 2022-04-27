# env\Scripts\activate
from flask import Flask,render_template
from flask_pymongo import PyMongo

app  =  Flask("__main__")

app.config["MONGO_URI"] = "mongodb+srv://saravanamuthusha:Register@cluster0.azsub.mongodb.net/vels"
app.secret_key = b'_5#y2L"F4Q8z/n/xec]/'
db = PyMongo(app).db



@app.route("/")
def index():
    return render_template("home.html")


@app.route("/admin")
def admin():
    return render_template("admin/home.html"    ,page="home")


@app.route("/live")
def live():
    return render_template("admin/live.html"    ,page="live")


@app.route("/aptitude")
def aptitude():
    return render_template("admin/aptitude.html"    ,page="aptitude")


@app.route("/add_student")
def add_student():
    return render_template("admin/add_student.html" ,page="add_student")







if __name__ == "__main__":
    app.run()