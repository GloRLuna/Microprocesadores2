#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO
BUTTON_GPIO = 20
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM) #GPIO.BOARD
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    pressed = False
    while True:
        # button is pressed when pin is LOW
        if not GPIO.input(BUTTON_GPIO):
            if not pressed:
                print("Button pressed!")
                pressed = True
        # button not pressed (or released)
        else:
            pressed = False
            print("Button unpressed!")
        time.sleep(0.3)
        
