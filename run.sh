#!/usr/bin/env bash

venv/bin/python run.py 5555 &>> "/var/log/home_lock.txt"
