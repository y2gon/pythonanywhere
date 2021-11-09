"""
# 06 Message Flashing
"""
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(days=5)  # ex. minutes=5


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user1 = request.form["nm"]
        session["user"] = user1  # session['dict_key']
        flash("Login Successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))

        return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:  # login 된 경우라면
        users = session["user"]
        return render_template("user.html", user=users)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))  # /login 으로 가는 view 함수 실행

@app.route("/logout")
def logout():
    flash("You have been logged out!", "info")
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
