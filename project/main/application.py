from flask import Blueprint, render_template

changtalk_app = Blueprint("changtalk", __name__, url_prefix="/app")

@changtalk_app.route("/changtalk")
def home():
    return render_template('index.html')

@changtalk_app.route("/search")
def search():
    return "search"

@changtalk_app.route("/boards")
def boards():
    return "boards"

@changtalk_app.route("/login")
def login():
    return "login"