#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO
BUTTON_GPIO = 20
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM) #op GPIO.BOARD
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    pressed = False
    while True: #Siempre
        # button is pressed when pin is HIGH
        if  GPIO.input(BUTTON_GPIO): #Lee el puerto del boton
            if not pressed:
                print("Button pressed!")
                pressed = True
        # button not pressed (or released)
        else: 
            pressed = False
            print("released!")
        time.sleep(1.0)
        
