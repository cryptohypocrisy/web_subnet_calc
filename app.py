#!/usr/bin/python3

from flask import Flask, render_template, request
import validation as v
from network import Network

network = Network()

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    network.ip, network.mask = [], []
    if request.method == "POST":
            network.ip = v.check_ip(request.form.get("ip"))
            network.mask, network.cidr = v.check_mask(request.form.get("mask"))
    return render_template("index.html", network=network)
