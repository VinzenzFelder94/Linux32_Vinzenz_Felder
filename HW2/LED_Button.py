#!/usr/bin/env python3
import time
import Adafruit_BBIO.GPIO as GPIO

button1="P9_18"  # P9_ for buttons
button2="P9_19"
button3="P9_20"
button4="P9_21"


LED1   ="P9_14" #P9_ for leds
LED2   ="P9_15"
LED3   ="P9_16"
LED4   ="P9_17"

# Set the GPIO pins:
GPIO.setup(LED1,    GPIO.OUT)
GPIO.setup(LED2,    GPIO.OUT)
GPIO.setup(LED3,    GPIO.OUT)
GPIO.setup(LED4,    GPIO.OUT)
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
GPIO.setup(button3, GPIO.IN)
GPIO.setup(button4, GPIO.IN)

# Turn on LEDs to default state
GPIO.output(LED1, 0)
GPIO.output(LED2, 0)
GPIO.output(LED3, 0)
GPIO.output(LED4, 0)

# Map buttons to LEDs
map = {button1: LED1, button2: LED2, button3: LED3, button4: LED4}

def updateLED(pin):
  
    state = GPIO.input(pin)
    if pin == "P9_18" or  pin == "P9_21":
      if state == 1:
        state = 0
      else:
        state = 1
    GPIO.output(map[pin], state)
    print(map[pin] + " Toggled")

print("Running...") #working programm

GPIO.add_event_detect(button1, GPIO.BOTH, callback=updateLED) # RISING, FALLING or BOTH
GPIO.add_event_detect(button2, GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(button3, GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(button4, GPIO.BOTH, callback=updateLED)


try:
	while True:
		time.sleep(100)

except KeyboardInterrupt:
    print("Cleaning Up")
    GPIO.cleanup()
GPIO.cleanup()
