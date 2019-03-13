import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session
from flask_mail import Mail,Message

app = Flask(__name__)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'connellyrogers@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ["Pass"]
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)




app.secret_key=os.environ["SECRET_KEY"]

@app.route('/', methods=["POST","GET"])
def renderHome():  

    return render_template("home.html")
    

@app.route('/page1',methods=["POST","GET"])
def renderPage1():
#get date/time
    return render_template("page1.html")
    
@app.route('/page2',methods=["POST","GET"])
def renderPage2():
    session["pg1data"] = request.form["pages"]
    session["pg3data"] = request.form["name"]
    if "pg1data" not in session:
        return redirect(url_for("renderPage1"))
    
    return render_template("page2.html")

@app.route('/page3',methods=["POST","GET"])
def renderPage3():
    session["pg2data"] = request.form["genre"]
    session["readEveryDay"] = request.form["readDaily"]
    if "pg2data" not in session:
        return redirect(url_for("renderPage2"))
        
    print(session["pg1data"])
    print(session["pg2data"])
    
    attachData="pg3data,pg1data,readEveryDay,pg2data\n\"%s\",\"%s\",\"%s\",\"%s\""%(session["pg3data"],session["pg1data"],session["readEveryDay"],session["pg2data"])
    
    msg = Message('Hello', sender = 'connellyrogers@gmail.com', recipients = ['connellyrogers@gmail.com'])
    msg.attach("data.csv","text/csv",attachData)
   
    mail.send(msg)
    
    return render_template("page3.html")
    # put info in csv then email out
    
   
    
    
if __name__=="__main__":
    app.run(debug=True)
