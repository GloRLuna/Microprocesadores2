from machine import Timer
import machine
count = 0
# Set the LED pin as an output
#led_pin = machine.Pin(25, machine.Pin.OUT)

# Create an event timer to blink the LED
#def blink(timer):
    # Toggle the LED state
#    led_pin.value(not led_pin.value())

def counter(timer):
    # increment count
    timer += 1
    return timer
    print(timer)

timer = Timer(-1)
#timer.init(period=1000, mode=Timer.PERIODIC, callback=blink)
timer.init(period=1000, mode=Timer.PERIODIC, callback=counter)
# The LED will blink indefinitely
#Deep sleep