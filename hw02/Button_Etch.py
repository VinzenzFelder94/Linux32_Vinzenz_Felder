#!/usr/bin/env python3
import sys, time, numpy
import Adafruit_BBIO.GPIO as GPIO


button1="P9_18" #Right P9_pins and 2 user buttons used
button2="P9_19" #left
button3="P9_20" #up
button4="P9_21" #down
pbutton="P9_22" #quit
mbutton="P9_23" #clear screen

# Set the GPIO pins:
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
GPIO.setup(button3, GPIO.IN)
GPIO.setup(button4, GPIO.IN)
GPIO.setup(pbutton, GPIO.IN)
GPIO.setup(mbutton, GPIO.IN)



# setting up the screen output

if len(sys.argv) == 3:
  x1 = int(sys.argv[1]) #get variable grid size over input arguments
  y1 = int(sys.argv[2])
else:
  x1 = 18
  y1 = 20
y0, x0 = 0, 0
screen = [[" " for x in range(x1)]for x in range(y1)]
# find screen center and move cursor
yc, xc = int((y1-y0)//2), int((x1-x0)//2)
x,y  = xc,yc
quit = False

# method called on button push to move cursor
def updatePosition(pin):

    state = GPIO.input(pin)
    time.sleep(0.05)
    if state != GPIO.input(pin):
      return

    global x,y,y1,x1,screen,quit
    
    key = pin
    
    if key  == 'P9_22': # quit
        quit = True
    elif key == 'P9_23': # clear screen
        print("Clearing screen...")
        screen = [[" "  for x in range(x1)] for x in range(y1)]
    elif key == 'P9_18':  #go right 
        if x < x1:
          x += 1
    elif key == 'P9_19':  #go left
        if x > 0:
          x -= 1
    elif key == 'P9_20':  #go up
        if y>0:
          y -= 1
    elif key == 'P9_21':  #go down
        if y< y1:
          y += 1    
 
    screen[x][y] = 'X'

GPIO.add_event_detect(button1, GPIO.RISING, callback=updatePosition) #Event Callback
GPIO.add_event_detect(button2, GPIO.FALLING, callback=updatePosition)
GPIO.add_event_detect(button3, GPIO.RISING, callback=updatePosition)
GPIO.add_event_detect(button4, GPIO.FALLING, callback=updatePosition)
GPIO.add_event_detect(mbutton, GPIO.FALLING, callback=updatePosition)
GPIO.add_event_detect(pbutton, GPIO.FALLING, callback=updatePosition)

# main method run after setup
def main():
    try:
      print("Running..")
      while True:
        if quit:
          print("Quit")
          GPIO.cleanup()
          break
        time.sleep(1)
        print(numpy.matrix(screen))
        
    except KeyboardInterrupt:
      print(" Cleaning Up")
      GPIO.cleanup()
    GPIO.cleanup()

# array printing method
def format_array(arr):
  for row in arr:
      for element in row:
         print(element, end= " ")
      print(" ")
  return 

if __name__ == "__main__":
   # pregame instructions
   print("EtchaSketch play 4 buttons to move the cursor, mode key to clear, and pause key to quit")
   if len(sys.argv) == 3 :
     print("Grid Size " + sys.argv[1] + " by " + sys.argv[2])
   else:
     print("No argument input, standart grid size, 18 by 20")
   
   main()


