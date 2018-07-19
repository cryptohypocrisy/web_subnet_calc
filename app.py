#!/usr/bin/python3

from flask import Flask, render_template, request
import validation as v
from network import Network

network = Network()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calc", methods=["POST"])
def calc():
    ip = request.form.get("ip")
    mask = request.form.get("mask")
    network.ip = v.check_ip(ip)
    network.mask, network.cidr = v.check_mask(mask)
    ip2 = network.ip
    mask2, cidr2 = network.mask, network.cidr
    if not network.ip or not network.mask:
        return render_template("error.html",
                                ip=ip2,
                                mask=mask2)
    return render_template("calc.html", ip=ip2, mask=mask2)
