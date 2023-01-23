from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

con = sqlite3.connect("users.db")
cur = con.cursor()
@app.route('/')
def hello():
    username = input("Enter username: ")
    password = input("Enter password: ")
    cur.execute("SELECT * FROM accounts WHERE uname=? and pwd=?", [username, password])

    if cur.fetchone() == None:
        print("Incorrect credentials")
    else:
        print("Logged in!")
    return render_template("html.html")

if __name__ == "__main__":
    app.run()
