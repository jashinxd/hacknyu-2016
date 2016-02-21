from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import urllib2
import json


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
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
                if (Append.authenticate(username, password)):
                        session['n']=username
                        return redirect(url_for(""))
                else:
                        error = "Your Username or Password is incorrect. Please try again."
                        return render_template("login.html", problem = error )