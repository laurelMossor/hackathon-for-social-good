from flask import (Flask, redirect, request, 
            render_template, jsonify, flash, session)
from jinja2 import StrictUndefined


app = Flask(__name__)


@app.route("/")
def homepage():

    return render_template("homepage.html")



###########################################################
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    # In debug mode, page will be updated when code is changed
    # To change, debug=False 