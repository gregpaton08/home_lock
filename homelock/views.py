from flask import render_template, jsonify, request
from homelock import app
import lock_motor

@app.route('/')
def hello_world():
    return 'Hello, world!!!'

@app.route('/lock_status')
def lock_status():
    return jsonify(locked=lock_motor.is_door_locked())

@app.route('/lock')
def lock():
    should_lock_door = request.args.get('lock', None)
    if should_lock_door is not none:
        lock_motor.lock_door(should_lock_door)

    return render_template('index.html')