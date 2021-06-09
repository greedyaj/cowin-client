from flask import Flask
from flask import request
from flask import render_template
from service import authentication
from service import search

app = Flask(__name__)

@app.route("/authenticate", methods=["POST", "GET"])
def authenticate():
    if request.method == "GET":
        return render_template('index.html', otpSent=False)
    elif request.method == "POST":
        if request.form["mobileNumber"] != None:
            txnId = authentication.generate_otp(mobileNumber=request.form["mobileNumber"])
            return render_template('authenticate.html', otpSent=True, txnId=txnId)
        elif request.form["otp"] != None:
            token = authentication.confirm_otp(txnId=request.form["txnId"], otp=request.form["otp"])
            return render_template('search-slots.html', slots=False)

@app.route("/search", methods=["POST", "GET"])
def lookup():
    if request.method == "GET":
        return render_template('search-slots.html', slots=True, slotsData=None)
    elif request.method == "POST":
        if request.form["pin"] != None:
            pin = request.form["pin"]
            slots = search.lookup_slots_by_pin(pin=pin)
            slotsToSee = (slots is not None)
            print("slotsToSee:" + str(slotsToSee))
            return render_template('search-slots.html', slots=slotsToSee, slotsData=slots, pin=pin)
