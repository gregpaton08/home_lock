#!/usr/bin/env bash

# Get the directory of this script and change to it.
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd ${DIR}

# Set up the virtual environment.
./environment/setup.sh

venv/bin/python run.py 5555 &>> "/var/log/home_lock.txt"
