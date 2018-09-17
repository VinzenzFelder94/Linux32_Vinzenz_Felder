#!/usr/bin/env python3
# Etch a sketch with buttons and 8x8 bicolor led display

import smbus, time
import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP1,eQEP2

bus = smbus.SMBus(2)  # Use i2c bus 2
matrix = 0x70         # Use address 0x70

delay = 1; # Delay between images in s

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

#init encoder1
myEncoder= RotaryEncoder(eQEP1)
myEncoder.setAbsolute()
myEncoder.enable()
#init encoder2
myEncoder2= RotaryEncoder(eQEP2)
myEncoder2.setAbsolute()
myEncoder2.enable()
#init putton
pbutton="P9_21"	#quit button
mbutton="P9_22" #clear screen button

GPIO.setup(pbutton, GPIO.IN)
GPIO.setup(mbutton, GPIO.IN)


# set up screen output
color = 'H'
x1, y1 = 8, 8
screen = [[' '  for x in range(x1)] for x in range(y1)]
yc, xc = 4, 4 #screen center
screen[xc][yc] = color
x,oldx,y,oldy  = xc,xc,xc,xc
quit = False
x2,y2,index_x,index_y = None,None,4,4

# The first byte is GREEN, the second is RED.
def clearDisplay():
# method to clear display complett zeros
   disp = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
       0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
   ]
   return disp

def displayArray(arr): 
# convert array data to i2c bus display
   global x2,y2,index_x,index_y,display
   disp = clearDisplay()
   for i in range(len(arr)):
      for j in range(len(arr[i])):
         if arr[i][j] == 'X':
           # print("X found at ",i,", ",j)
            index_x = 2*i+1
            disp[index_x] += 2**j
         if arr[i][j] == 'G':
            index_y = 2*i
            disp[index_y] += 2**j
         if arr[i][j] == 'H':
            index_x = 2*i+1
            disp[index_x] += 2**j
            index_y = 2*i
            disp[index_y] += 2**j
                        
   return disp

def printArray(arr):
# method to print array onto console output
  for row in arr:
      for element in row:
          print(element, end=" ")
      print(' ')
  return 
 

def updatePosition(pin):
# method called on button push to move cursor and update displays
    

    global x,y,x1,y1,oldx,oldy,screen,quit,display,color,enc1,enc2
    
    key = pin
    oldx = x;
    oldy = y;
    # check which button pushed, act accordingly
    
    if key  == 'P9_21': # quit
        quit = True
    elif key == 'P9_22': # clear screen
        print("Clearing screen...")
        screen = [[' '  for x in range(y1)] for x in range(x1)]
    elif key == 'Joy2+': #go right
        if x > 0:
          x -= 1
    elif key == 'Joy2-': #go left
        if x < (x1-1):
          x += 1
    elif key == 'Joy3+': #go up
        if y > 0:
          y -= 1
    elif key == 'Joy3-': #go down
        if y < (y1-1):
          y += 1
        
    # update displays
    screen[oldx][oldy] = color
    screen[x][y] = 'X'
    display = displayArray(screen)
    printArray(screen)
    bus.write_i2c_block_data(matrix, 0, display)
    print("Position: "+str(x)+", "+str(y))

# event listen
# RISING, FALLING or BOTH
GPIO.add_event_detect(mbutton, GPIO.FALLING, callback=updatePosition)
GPIO.add_event_detect(pbutton, GPIO.FALLING, callback=updatePosition)

def main():
# main method run after setup
    global quit,color
    try:
      print("Running..")
      # inital display update
      printArray(screen)
      display = displayArray(screen)
      bus.write_i2c_block_data(matrix, 0, display)
      enc1old = 0
      enc2old = 0
      print("Position: "+str(x)+", "+str(y)) 
      while True:
      # main loop listening for quit
        if quit:
          print("Quit")
          bus.write_i2c_block_data(matrix, 0, clearDisplay())
          GPIO.cleanup()
          break
        # read encoders
        enc1 =myEncoder.position
        enc2 =myEncoder2.position
        if enc1 > enc1old:         #encoder change positiv
            updatePosition('Joy2+')
            #print(enc1)
        elif enc1 < enc1old:       #encoder change negative
            updatePosition('Joy2-')
        if enc2 > enc2old:
            updatePosition('Joy3+')
        elif enc2 < enc2old:
            updatePosition('Joy3-')
        enc1old = myEncoder.position #upadte from current position
        enc2old = myEncoder2.position
        
    except KeyboardInterrupt:
          print("Quitting Etch-a-Sketch, thanks!")
          bus.write_i2c_block_data(matrix, 0, clearDisplay())
          GPIO.cleanup()

if __name__ == "__main__":
   # instructions
   print("EtchaSketch play with two encoders for x and y movement,")
   print("and two buttons for clearing screen and quiting game")
   input("Press enter to begin playing...")


   main()

