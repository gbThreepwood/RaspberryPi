#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

def buttonEventHandler (pin):
    print "Event detected on GPIO pin 25"

    GPIO.output(25,True)

    time.sleep(1)

    GPIO.output(25,False)


def main():

    GPIO.setmode(GPIO.BCM)

    # Setup the gpio signals 
    GPIO.setup(23,GPIO.IN)
    GPIO.setup(24,GPIO.OUT)
    GPIO.setup(25,GPIO.OUT)

    # Call the button event handler function whenever
    # GPIO pin 23 goes low. 
    GPIO.add_event_detect(23,GPIO.FALLING)
    GPIO.add_event_callback(23,buttonEventHandler)


    GPIO.output(25,False)
    GPIO.output(24,True)

    # Infinite while loop to blink the LED connected to GPIO pin 24    
    while True:
        GPIO.output(24,True)
        time.sleep(1)
        GPIO.output(24,False)
        time.sleep(1)


    GPIO.cleanup()



if __name__=="__main__":
   try:
      main()
   except:
      GPIO.cleanup()
