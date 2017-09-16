#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

switch_input = 17

GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(switch_input, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def run_motor():
    count = 0
    while count < 3:
        GPIO.output(4, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(4, GPIO.LOW)
        time.sleep(1)
        count = count + 1

def check_switch():
    count = 0
    while True:
        state = GPIO.input(switch_input)
        if state:
            print('Switch press {0}'.format(count))
            count = count + 1
            GPIO.output(4, GPIO.HIGH)
        else:
            GPIO.output(4, GPIO.LOW)
        time.sleep(0.2)

try:
    check_switch()
    #run_motor()
except KeyboardInterrupt:
    GPIO.cleanup()


