from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)
# Custom filter

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///budget.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/budget", methods=["POST","GET"])
@login_required
def budget():
    if request.method == "POST":
        if not request.form.get("budget"):
            return apology("Missing Input")
        budget = request.form.get("budget")
        try:
            if not int(budget) > 0:
                return apology("Budget must be higher than 0")
        except:
            return apology("Budget must be an Integer")
        budget = int(budget)
        db.execute("UPDATE users SET budget = ? WHERE user_id = ?",
                   budget,
                   session["user_id"])
        return redirect("/")
    else:
        current_budget = int(db.execute("SELECT budget FROM users WHERE user_id = ?",
                                    session["user_id"])[0]["budget"])
        return render_template("budget.html", budget=current_budget)

@app.route("/", methods=["GET"])
@login_required
def index():
    total_costs = 0
    all_categories = db.execute("SELECT * FROM categories WHERE user_id = ?",
                                session["user_id"])
    for category in all_categories:
        category_cost = 0
        category_max = int(db.execute("SELECT budget FROM categories WHERE user_id = ? AND name = ?",
                                  session["user_id"],
                                  category["name"])[0]["budget"])
        all_items = db.execute("SELECT * FROM items WHERE category = ? AND user_id = ?",
                               category["name"],
                               session["user_id"])
        for item in all_items:
            price = int(item["price"])
            category_cost += price
            if category_cost > category_max:
                item["status"] = "Budget Exceeded"
                item["color"] = "red"
            else:
                item["status"] = "OK"
                item["color"] = "green"
        category["items"] = all_items
        total_costs += category_cost
        if category_cost > category_max:
            category["status"] = "Budget Exceeded"
            category["color"] = "red"
        else:
            category["status"] = "OK"
            category["color"] = "green"
        category["actual_costs"] = category_cost
        subtract = category_max - category_cost
        if subtract < 0:
            subtract = 0
        category["free"] = subtract
    maximum_budget = int(db.execute("SELECT budget FROM users WHERE user_id = ?",
                                session["user_id"])[0]["budget"])
    left_budget = maximum_budget - total_costs
    if left_budget < 0:
        left_budget = 0
        status = "Budget Exceeded"
        color = "red"
    else:
        status = "OK"
        color = "green"
    return render_template("index.html", all_categories=all_categories,
                           left=left_budget,
                           max=maximum_budget,
                           costs=total_costs,
                           status=status,
                           color=color)

@app.route("/items", methods=["GET","POST"])
@login_required
def items():
    if request.method == "POST":
        if not request.form.get("name") or not request.form.get("price") or not request.form.get("category"):
            return apology("Missing Input")
        name = request.form.get("name")
        price = request.form.get("price")
        img = request.form.get("image")
        category = request.form.get("category")
        try:
            if not int(price) > 0:
                return apology("Budget must be higher than 0")
        except:
            return apology("Budget must be an Integer")
        price = int(price)
        result = db.execute("SELECT name FROM categories WHERE user_id = ?",
                            session["user_id"])
        all_categories = []
        for item in result:
            all_categories.append(item["name"])
        if not category in all_categories:
            return apology("Invalid Category")
        db.execute("INSERT INTO items (user_id,image,name,price,category) VALUES (?,?,?,?,?)",
                   session["user_id"],
                   img,
                   name,
                   price,
                   category)
        return redirect("/items")
    if request.method == "GET":
        output = db.execute("SELECT * FROM categories WHERE user_id = ?",
                session["user_id"])
        items = db.execute("SELECT * FROM items WHERE user_id = ?",
                           session["user_id"])
        return render_template("items.html", output=output, items=items)

@app.route("/delete_item", methods=["POST"])
@login_required
def delete_item():
    item_id = request.form.get("id")
    db.execute("DELETE FROM items WHERE item_id = ?",
               item_id)
    return redirect("/items")

@app.route("/categories", methods=["GET","POST"])
@login_required
def categories():
    if request.method == "POST":
        if not request.form.get("name") or not request.form.get("budget"):
            return apology("Missing Input")
        name = request.form.get("name")
        budget = request.form.get("budget")
        try:
            if not int(budget) > 0:
                return apology("Budget must be higher than 0")
        except:
            return apology("Budget must be an Integer")
        budget = int(budget)
        db.execute("INSERT INTO categories (user_id,name,budget) VALUES (?,?,?)",
                   session["user_id"],
                   name,
                   budget)
        return redirect("/categories")
    else:
        output = db.execute("SELECT * FROM categories WHERE user_id = ?",session["user_id"])
        max_budget = db.execute("SELECT budget FROM users WHERE user_id = ?",
                                session["user_id"])
        max_budget = int(max_budget[0]["budget"])
        current_budget = 0
        for category in output:
            current_budget += int(category["budget"])
            if current_budget > max_budget:
                category["status"] = "Budget Exceeded"
                category["color"] = "red"
            else:
                category["status"] = "OK"
                category["color"] = "green"
        left_budget = max_budget - current_budget
        if left_budget < 0:
            left_budget = 0
    return render_template("categories.html", output=output, max_budget=max_budget, current_budget=current_budget, left=left_budget)

@app.route("/edit_category", methods=["POST"])
@login_required
def edit_category():
    if not request.form.get("name") or not request.form.get("budget") or not request.form.get("id"):
        return apology("Missing Input")
    name = request.form.get("name")
    budget = request.form.get("budget")
    try:
        if not int(budget) > 0:
            return apology("Budget must be higher than 0")
    except:
        return apology("Budget must be an Integer")
    budget = int(budget)
    id = request.form.get("id")
    old_category = db.execute("SELECT name FROM categories WHERE category_id = ?",
                              id)
    old_category = old_category[0]["name"]
    db.execute("UPDATE items SET category = ? WHERE category = ? AND user_id = ?",
               name,
               old_category,
               session["user_id"])
    db.execute("UPDATE categories SET name = ?, budget = ? WHERE category_id = ?",
           name,
           budget,
           id)
    return redirect("/categories")

@app.route("/edit_cat", methods=["GET","POST"])
@login_required
def edit_cat():
    if request.method == "POST":
        id = request.form.get("id")
        out = db.execute("SELECT * FROM categories WHERE category_id = ?",id)
        return render_template("update_categories.html", id=id,output=out)
    return "Error"

@app.route("/delete_cat", methods=["POST"])
@login_required
def delete_cat():
    if request.method == "GET":
        return apology("Invalid")
    category_id = request.form.get("id")
    old_category = db.execute("SELECT name FROM categories WHERE category_id = ?",
                              category_id)
    old_category = old_category[0]["name"]
    db.execute("DELETE FROM items WHERE category = ? AND user_id = ?",
               old_category,
               session["user_id"])
    db.execute("DELETE FROM categories WHERE category_id = ?",category_id)
    return redirect("/categories")

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )
        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["password"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["user_id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if (
            not request.form.get("username")
            or not request.form.get("password")
            or not request.form.get("confirmation")
            or not request.form.get("budget")
        ):
            return apology("Missing Input")
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Passwords do not match!")
        username = request.form.get("username")
        pw = generate_password_hash(request.form.get("password"))
        budget = request.form.get("budget")
        try:
            if not int(budget) > 0:
                return apology("Budget must be higher than 0")
        except:
            return apology("Budget must be an Integer")
        budget = int(budget)
        try:
            db.execute("INSERT INTO users (username,password,budget) VALUES (?,?,?)", username, pw, budget)
        except:
            return apology("Username is already taken!")
        return redirect("/")
    return render_template("register.html")

