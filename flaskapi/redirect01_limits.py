#!/usr/bin/python3
"""
Making use of HTTP non-200 type responses.
https://tools.ietf.org/html/rfc2616 # rfc spec describing HTTP
1xx - informational
2xx - success / ok
3xx - redirection
4xx - errors
5xx - server errors
"""

from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from flask import abort
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["20 per day", "5 per hour"]
)

# if user sends GET to / (root)
@app.route("/")
def index():
    return render_template("log_in.html")   # found in templates/




# if user sends GET or POST to /login
@app.route("/login", methods = ["POST", "GET"])
def login():
    # if user sent a POST
    if request.method == "POST":
        # if the POST contains 'admin' as the value for 'username'
        if request.form["username"] == "admin" :
            return redirect(url_for("success")) # return a 302 redirect to /success
        elif request.form["username"] == "Bob" :
            return redirect(url_for("failed")) # return a 302 redirect to /success
        else:
            abort(406)  # if they didn't supply the username 'admin' send back a 401
    elif request.method == "GET":
        return redirect(url_for("index")) # if they sent a GET to /login send 302 redirect to /


@app.route("/success")
def success():
    return "logged in successfully"

@app.route("/failed")
@limiter.limit("2 per day")
def failed():
    abort(403)
    return "You are Bob..once more!"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)

