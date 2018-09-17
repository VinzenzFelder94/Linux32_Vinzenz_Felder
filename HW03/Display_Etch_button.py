# Etch a sketch with buttons and 8x8 bicolor led display

import smbus, time
import Adafruit_BBIO.GPIO as GPIO
bus = smbus.SMBus(2)  # Use i2c bus 2
matrix = 0x70         # Use address 0x70

delay = 1; # Delay between images in s

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

#init button
button1="P9_23" #Right P9_pins and 2 user buttons used
button2="P9_24" #left
button3="P9_25" #up
button4="P9_26" #down
pbutton="P9_21" #quit
mbutton="P9_22" #clear screen


# Set the GPIO pins:
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
GPIO.setup(button3, GPIO.IN)
GPIO.setup(button4, GPIO.IN)
GPIO.setup(pbutton, GPIO.IN)
GPIO.setup(mbutton, GPIO.IN)


# set up screen output
color = 'O'
x1, y1 = 8, 8
screen = [[' '  for x in range(x1)] for x in range(y1)]
yc, xc = 4, 4 #screen center
screen[xc][yc] = color
x,oldx,y,oldy  = xc,xc,xc,xc
quit = False
x2,y2,index_x,index_y = None,None,4,4

# The first byte is GREEN, the second is RED.
def clearDisplay():
# method to clear display
   disp = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
       0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
   ]
   return disp

def displayArray(arr): 
# convert array data to i2c bus display
   global lastx,lasty,index_x,index_y,display
   disp = clearDisplay()
   for i in range(len(arr)):
      for j in range(len(arr[i])):
         if arr[i][j] == 'X':
            index_x = 2*i+1
            disp[index_x] += 2**j
         if arr[i][j] == 'O':
            index_y = 2*i
            disp[index_y] += 2**j
         if arr[i][j] == 'H':
            print("H found at ",i,", ",j)
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

    state = GPIO.input(pin)
    time.sleep(0.05)
    if state != GPIO.input(pin):
      return

    global x,y,x1,y1,oldx,oldy,screen,quit,display,color
    
    key = pin
    oldx = x;
    oldy = y;
    # button push
    if key  == 'P9_21': # quit
        quit = True
    elif key == 'P9_22': # clear screen
        print("Clearing screen...")
        screen = [[" "  for x in range(x1)] for x in range(y1)]
    elif key == 'P9_23':  #go right 
        if x < x1:
          x += 1
    elif key == 'P9_24':  #go left
        if x > 0:
          x -= 1
    elif key == 'P9_25':  #go up
        if y>0:
          y -= 1
    elif key == 'P9_26':  #go down
        if y< y1:
          y += 1    

    # update displays
    screen[oldx][oldy] = color
    screen[x][y] = 'H'
    display = displayArray(screen)
    printArray(screen)
    bus.write_i2c_block_data(matrix, 0, display)
    print("Position: "+str(x)+", "+str(y)) 
    
    
# event listen
GPIO.add_event_detect(button1, GPIO.RISING, callback=updatePosition) # RISING, FALLING or BOTH
GPIO.add_event_detect(button2, GPIO.FALLING, callback=updatePosition)
GPIO.add_event_detect(button3, GPIO.RISING, callback=updatePosition)
GPIO.add_event_detect(button4, GPIO.FALLING, callback=updatePosition)
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
      print("Position: "+str(x)+", "+str(y)) 
      while True:
      # main loop listening for quitflag
        if quit:
          print("Quit")
          bus.write_i2c_block_data(matrix, 0, clearDisplay())
          GPIO.cleanup()
          break
  
    except KeyboardInterrupt:
          print("Quitting Etch-a-Sketch, thanks!")
          bus.write_i2c_block_data(matrix, 0, clearDisplay())
          GPIO.cleanup()
if __name__ == "__main__":
   # instructions
   print("EtchaSketch play with buttons ")
   print("Use the 4 buttons to move the cursor, button to clear, and pause button to quit")
   input("Press enter to begin playing...")
   main()
