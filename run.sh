#!/usr/bin/env bash

if [ ! -d flask ]; then
    virtualenv flask

    flask/bin/pip flask
fi

flask/bin/python2.7 run.py 5555