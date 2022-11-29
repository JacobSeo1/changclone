from flask import Flask
from . import application

app = Flask(__name__)

app.register_blueprint(application.changtalk_app)