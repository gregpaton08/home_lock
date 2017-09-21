from flask import render_template, jsonify
from homelock import app

@app.route('/')
def hello_world():
    return 'Hello, world!!!'