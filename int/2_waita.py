#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO
BUTTON_GPIO = 20
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM) #op GPIO.BOARD
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    pressed = False
    #print("configurado")
    while True:
        GPIO.wait_for_edge(BUTTON_GPIO, GPIO.RISING) #SUBIDA
        if GPIO.input(BUTTON_GPIO):
            print("Button pressed!")
        