#!/usr/bin/python3

from flask import Flask, render_template, request, session
from flask_session import Session
import validation as v
from network import Network

# network = Network()

app = Flask(__name__, static_url_path='/static')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["POST", "GET"])
def index():

    if not session.get("network"):
        session["network"] =  Network()
    session["network"].ip, session["network"].mask = [], []

    if request.method == "POST":
        try:
            session["network"].ip = v.check_ip(request.form.get("ip"))
            session["network"].mask, session["network"].cidr = v.check_mask(request.form.get("mask"))
        except TypeError:
            session["network"].ip = False
            session["network"].mask, session["network"].cidr = False, False

    return render_template("index.html", network=session["network"])
