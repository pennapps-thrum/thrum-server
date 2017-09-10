#!/usr/bin/python

from flask import Flask, render_template, request
from app import app
import firebase

@app.route("/")
def index():
    return "This page intentionally left blank"

# TODO: change to get request
@app.route("/toggle")
def toggle():
    if 'status' in request.args:
        if request.args['status'] == "on":
            # turn on thrum
            firebase.send_message("on")
	    return "turning on thrum"
        elif request.args['status'] == "off":
            # turn off thrum
            firebase.send_message("off")
	    return "turning off thrum"
	else:
	    return "Error"
    else:
        return "Error"
