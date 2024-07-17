import os
from datetime import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
@login_required
def index():
    value = 0
    output = db.execute(
        "SELECT symbol,shares FROM depot WHERE user_id = ?", session["user_id"]
    )
    for item in output:
        item["price_per_share"] = int(lookup(item["symbol"])["price"])
        item["value"] = item["price_per_share"] * int(item["shares"])
        value += item["value"]
        item["price_per_share"] = usd(item["price_per_share"])
        item["value"] = usd(item["value"])
    cashpos = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    cashpos = int(cashpos[0]["cash"])
    total = usd(cashpos + value)
    value = usd(value)
    cashpos = usd(cashpos)
    return render_template(
        "index.html", output=output, cashpos=cashpos, equity=value, total=total
    )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        if not request.form.get("shares") or not request.form.get("symbol"):
            return apology("Missing input")
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        try:
            if not int(shares) > 0:
                return apology("Shares must be higher than 0")
        except:
            return apology("Shares must be an Integer")
        output = lookup(symbol)
        if not output:
            return apology("Invalid Symbol")
        userdict = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        amount = int(userdict[0]["cash"])
        costs = int(output["price"]) * int(shares)
        if costs > amount:
            return apology("Ur too broke")
        out = db.execute(
            "SELECT shares FROM depot WHERE user_id = ? AND symbol = ?",
            session["user_id"],
            symbol,
        )
        if out:
            out = int(out[0]["shares"])
            db.execute(
                "UPDATE depot SET shares = ? WHERE user_id = ? AND symbol = ?",
                out + int(shares),
                session["user_id"],
                symbol,
            )
        else:
            db.execute(
                "INSERT INTO depot (user_id,symbol,shares,last_modified) VALUES (?,?,?,?)",
                session["user_id"],
                symbol,
                int(shares),
                datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
            )

        db.execute(
            "INSERT INTO transactions (user_id,symbol,price_per_share,shares,total_costs,date,type) VALUES (?,?,?,?,?,?,?)",
            session["user_id"],
            symbol,
            int(output["price"]),
            int(shares),
            costs,
            datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
            "buy",
        )
        db.execute(
            "UPDATE users SET cash = ? WHERE id = ?", amount - costs, session["user_id"]
        )
        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/deposit", methods=["POST", "GET"])
@login_required
def deposit():
    if request.method == "POST":
        if not request.form.get("amount"):
            return apology("Missing Input")
        amount = request.form.get("amount")
        try:
            if not int(amount) > 0:
                return apology("Amount must be higher than 0")
        except:
            return apology("Amount must be an Integer")
        current_cash = db.execute(
            "SELECT cash FROM users WHERE id = ?", session["user_id"]
        )
        current_cash = int(current_cash[0]["cash"])
        cash = current_cash + int(amount)
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, session["user_id"])
        return redirect("/")
    return render_template("deposit.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    output = db.execute(
        "SELECT * FROM transactions where user_id = ?", session["user_id"]
    )
    for item in output:
        item["price_per_share"] = usd(item["price_per_share"])
        item["total_costs"] = usd(item["total_costs"])
    return render_template("history.html", output=output)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
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
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("Blank Ticker Symbol")
        symbol = request.form.get("symbol")
        output = lookup(symbol)
        if output == None:
            return apology("Symbol does not exist!")
        output["price"] = usd(output["price"])
        return render_template("quoted.html", output=output)
    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if (
            not request.form.get("username")
            or not request.form.get("password")
            or not request.form.get("confirmation")
        ):
            return apology("Missing Input")
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Passwords do not match!")
        username = request.form.get("username")
        pw = generate_password_hash(request.form.get("password"))
        try:
            db.execute("INSERT INTO users (username,hash) VALUES (?,?)", username, pw)
        except:
            return apology("Username is already taken!")
        return redirect("/")
    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "GET":
        stocks = db.execute(
            "SELECT symbol from depot WHERE user_id = ?", session["user_id"]
        )
        return render_template("sell.html", stocks=stocks)
    if request.method == "POST":
        if not request.form.get("symbol") or not request.form.get("shares"):
            return apology("Missing Input")
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        try:
            if not int(shares) > 0:
                return apology("Shares must be higher than 0")
        except:
            return apology("Shares must be an Integer")
        shares = int(shares)
        out = db.execute(
            "SELECT shares FROM depot WHERE user_id = ? AND symbol = ?",
            session["user_id"],
            symbol,
        )
        account_shares = int(out[0]["shares"])
        if shares > account_shares:
            return apology("Not enough shares!")
        total_return = int(lookup(symbol)["price"]) * shares
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = int(cash[0]["cash"])
        db.execute(
            "UPDATE depot SET shares = ? WHERE user_id = ? AND symbol = ?",
            account_shares - shares,
            session["user_id"],
            symbol,
        )
        db.execute(
            "UPDATE users SET cash = ? WHERE id = ?",
            cash + total_return,
            session["user_id"],
        )
        db.execute(
            "INSERT INTO transactions (user_id,symbol,price_per_share,shares,total_costs,date,type) VALUES (?,?,?,?,?,?,?)",
            session["user_id"],
            symbol,
            int(lookup(symbol)["price"]),
            shares,
            total_return,
            datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
            "sell",
        )
        return redirect("/")

    return apology("TODO")
