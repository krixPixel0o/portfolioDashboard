from flask import Flask, render_template, request
import mysql.connector

d = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "krishkunt#24",
    database = "portoDB"
)

c = d.cursor()

a = Flask(__name__)

@a.route('/')
def home() :
    return render_template("index.html")

@a.route('/contact', methods = ['POST'])
def contact() :
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    s = "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)"

    v = (name, email, message)
    c.execute(s, v)
    d.commit()

    return render_template("index.html")

if __name__ == "__main__" :
    a.run(host="0.0.0.0", port=5000)