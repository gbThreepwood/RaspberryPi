#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

def main():

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(23,GPIO.IN)
    GPIO.setup(24,GPIO.OUT)
    GPIO.setup(25,GPIO.OUT)


    GPIO.output(25,True)

    while True:
        if GPIO.input(23):
             GPIO.output(24,True)
             GPIO.output(25,False)
             print "Button true"
        else:
             GPIO.output(24,False)
             GPIO.output(25,True)
             print "Button false"

        time.sleep(0.1)

    print "Detected gpio event"

    GPIO.cleanup()



if __name__=="__main__":
    main()
