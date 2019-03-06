import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];   

@app.route('/', methods=["POST","GET"])
def renderStore():
    if "itemsincart" not in session or "clear" in request.args:
        session["itemsincart"] = 0
        print("skrt")
        session["item_a"] = 0
        session["item_b"] = 0
        session["item_c"] = 0
        
        
    return render_template("store.html",itemsincart=session["itemsincart"])
    

@app.route('/addToCart',methods=["POST","GET"])
def renderAddToCart():
    session["itemsincart"] += 1
    if request.args["item"]=="a":
        session["item_a"] += 1
    
    elif request.args["item"]=="b":
        session["item_b"] += 1
        
    elif request.args["item"]=="c":
        session["item_c"] += 1
    return render_template("addToCart.html", item_name = "Item " + str(request.args["item"]))
    
@app.route('/checkout',methods=["POST","GET"])
def renderCheckout():
    if "itemsincart" not in session:
        return redirect(url_for("renderStore"))
    return render_template("checkout.html",itemsincart=session["itemsincart"])

@app.route('/bought',methods=["POST","GET"])
def renderBought():
    if "itemsincart" not in session:
        return redirect(url_for("renderStore"))
    items = session["itemsincart"]
    session["itemsincart"] = 0
    return render_template("bought.html",itemsincart=str(items))
    
if __name__=="__main__":
    app.run(debug=True)
