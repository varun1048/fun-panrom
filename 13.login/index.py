# vels\Scripts\activate
# from os import system
# system('cls')
from flask  import  Flask, redirect ,render_template, request,url_for , flash
from flask_pymongo import PyMongo

app  = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://saravanamuthusha:Register@cluster0.azsub.mongodb.net/vels"
app.secret_key = b'_5#y2L"F4Q8z/n/xec]/'
db = PyMongo(app).db
    
@app.route("/")
def index():
    return render_template("index.html",data= db['student'].find())

@app.route("/login",methods=['GET','POST'])
def login():    
    if request.method == 'POST':
        form  = request.form  
        user =  db['student'].find_one({
            "username":form['username'],
            "password":form['password']
            })



        if user:
            print(user)
            return redirect(url_for("username",username = form['username']))
        flash('No data')


    return render_template("login.html")


@app.route("/register",methods=['GET','POST'])
def register():
    if request.method == 'POST':
        form  = request.form
        db['student'].insert_one({
            "username":form['username'],
            "password":form['password']
            })
        
        return redirect(url_for("login"))  

    return render_template("register.html")



@app.route("/user/<string:username>")
def username(username):
    return username




if __name__ == "__main__":  
    # app.run()
    
    ip = "192.168.1.7"
    # ip = "192.168.81.57"
    app.run(host=ip, port=5000, debug=True, threaded=False)