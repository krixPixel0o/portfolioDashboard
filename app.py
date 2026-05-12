from flask import Flask, render_template, request
import mysql.connector


a = Flask(__name__)

@a.route('/')
def home() :
    return render_template("index.html")

@a.route('/contact', methods=['POST'])
def contact():

    return render_template(
        "index.html",
        success="Message Sent Successfully!"
    )

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    a.run(
        host="0.0.0.0",
        port=port
    )