#!/usr/bin/env bash

# Set up the virtual environment.
./environment/setup.sh

venv/bin/python run.py 5555 &>> "/var/log/home_lock.txt"
