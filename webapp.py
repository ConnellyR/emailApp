import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];   
pg1data = 0
pg2data = ""


@app.route('/', methods=["POST","GET"])
def renderHome():   
    return render_template("home.html")
    

@app.route('/page1',methods=["POST","GET"])
def renderPage1():
    return render_template("page1.html")
    
@app.route('/page2',methods=["POST","GET"])
def renderPage2():
    session["pg1data"] = request.form["pages"]
    if "pg1data" not in session:
        return redirect(url_for("renderPage1"))
    return render_template("page2.html")

@app.route('/page3',methods=["POST","GET"])
def renderPage3():
    session["pg2data"] = request.form["genre"]
    if "pg2data" not in session:
        return redirect(url_for("renderPage2"))

    
    return render_template("page3.html")
    
if __name__=="__main__":
    app.run(debug=True)
