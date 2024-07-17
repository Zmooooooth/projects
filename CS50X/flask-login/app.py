from flask import Flask, render_template, request, redirect, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["POST","GET"])
def index():
        return render_template("index.html", name=session.get("name"))

@app.route("/login", methods=["POST","GET"])
def login():
        if request.method == "POST":
                session["name"] = request.form.get("name")
                return redirect("/")
        return render_template("login.html")

@app.route("/logout", methods=["GET"])
def logout():
        session.clear()
        return redirect("/")