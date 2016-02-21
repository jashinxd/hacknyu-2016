from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import urllib2
import database
import json 
import os

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/index",methods=["GET","POST"])
def index():
    return render_template("index.html")
    
@app.route("/login", methods = ["POST", "GET"])
def login():
	if (request.method == "GET"):
		return render_template("login.html")
	else:
		username = request.form["username"]
		password = request.form["password"]
		session['username'] = request.form["username"]
        if (database.authenticate(username, password)):
            session['user']=username
            return redirect(url_for(""))
        else:
            error = "Your Username or Password is incorrect. Please try again."
            return render_template("login.html", problem = error )
                        
@app.route("/registerdentist")
def registerDentist():
    if (request.method == "GET"):
        return render_template("registerdentist.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        specialization = request.form["specialization"]
        clinicaddress = request.form["clinicaddress"]
        emailaddress = request.form["emailaddress"]
        clinicphonenumber = request.form["clinicphonenumber"]
        if database.validDentistUname(username):
            error = "Username already exists. Please try again."
            return render_template("register.html", err = error)
        else:
            database.registerDentist(username,password,firstname,lastname,specialization,\
            clinicaddress,emailaddress,clinicphonenumber)
            return redirect(url_for("login"))  

@app.route("/registerpatient", methods=["POST","GET"])
def registerPatient():
    if (request.method == "GET"):
        return render_template("registerpatient.html")
    else:
        username = str(request.form["username"])
        password = str(request.form["password"])
        firstname = str(request.form["firstname"])
        lastname = str(request.form["lastname"])
        homeaddress = str(request.form["homeaddress"])
        emailaddress = str(request.form["emailaddress"])
        phonenumber = str(request.form["phonenumber"])
        if database.validPatientUname(username):
            error = "Username already exists. Please try again."
            return render_template("register.html", err = error)
        else:
            database.registerPatient(username,password,firstname,lastname,homeaddress,\
            emailaddress,phonenumber)
            return redirect(url_for("login"))    

if __name__ == "__main__":
    """
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8000)))
    """
    app.debug = True
    app.secret_key = "Don't put on git"
    app.run(host="0.0.0.0", port=8080)
