from flask import  Flask, render_template, request

from flames import do_flames
app = Flask("__main__")

import os
os.system("cls")

@app.route("/",methods=['GET','POST'])
def index():
    output = ""
    if request.method == 'POST':
        form = request.form
        output = do_flames(form["name1"],form["name2"])
    
    return render_template("index.html",output=output)

if __name__ == "__main__":
    app.run()
    # ip = "192.168.1.2"
    # app.run(host=ip, port=5000, debug=True, threaded=False)