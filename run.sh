#!/usr/bin/env bash

if [ ! -d flask ]; then
    virtualenv flask

    flask/bin/pip install flask
    flask/bin/pip install flask-restful
fi

flask/bin/python2.7 run.py 5555