import sys
import os
root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(root_dir, 'lib'))

from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from flask import Flask, render_template, jsonify
from flask import redirect
from flask import request
import json

app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     return render_template('index.html')


run_wsgi_app(app)