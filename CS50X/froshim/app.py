from flask import Flask, render_template, request, redirect

app = Flask(__name__)

REGISTRANTS = {}

SPORTS = ["Basketball","Soccer","Football","Ultimate Frisbee"]

@app.route("/", methods=["POST","GET"])
def index():
        return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():
        if not request.form.get("name") or request.form.get("sport") not in SPORTS:
                return render_template("failure.html")
        else:
                user_name = request.form.get("name")
                user_sport = request.form.get("sport")
                REGISTRANTS[user_name] = user_sport
                print(REGISTRANTS)
                return redirect("/registrants")

@app.route("/registrants")
def registrants():
        return render_template("registrants.html", registrants=REGISTRANTS)
