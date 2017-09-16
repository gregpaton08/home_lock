#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)

def run_motor():
    count = 0
    while count < 3:
        GPIO.output(4, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(4, GPIO.LOW)
        time.sleep(1)
        count = count + 1

try:
    run_motor()
except KeyboardInterrupt:
    GPIO.cleanup()


