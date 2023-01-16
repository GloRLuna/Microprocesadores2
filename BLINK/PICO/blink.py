import time
from machine import Pin
led=Pin(13,Pin.OUT)        #create LED object from pin13,Set Pin13 to output

while True:
  led.value(1)            #Set led turn on
  time.sleep(0.75)
  led.value(0)            #Set led turn off
  time.sleep(0.75)
