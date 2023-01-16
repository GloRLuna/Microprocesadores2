#!/usr/bin/env python3          
                                
import signal                   
import sys
import RPi.GPIO as GPIO
BUTTON_GPIO = 20
LED_GPIO =21
last_LED_state = 0
def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)
def button_callback(channel):
    global last_LED_state
    GPIO.output(LED_GPIO, not last_LED_state)
    last_LED_state = not last_LED_state

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(LED_GPIO, GPIO.OUT)   

    GPIO.add_event_detect(BUTTON_GPIO, GPIO.RISING, 
            callback=button_callback, bouncetime=200)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
    
