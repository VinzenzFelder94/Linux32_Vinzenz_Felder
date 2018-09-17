Hello, 

here is the HW02 for Linux 32-Embedded Class. 

In the directory you can find a file LED_Button.py , 
to toggle LEDs via buttons make sure you connected to the right pins.

Here is the Pin Config:
button1="P9_18"  
button2="P9_19"
button3="P9_20"
button4="P9_21"


LED1   ="P9_14"
LED2   ="P9_15"
LED3   ="P9_16"
LED4   ="P9_17"



to execute use:

bone $:python3 LED_Button.py 

than push the buttons to toggle the LEDs. 

and 

button_etch.py to control a etch a sketch file via buttons. 

Here are the Button PinOuts:

button1="P9_18" #Right P9_pins and 2 user buttons used
button2="P9_19" #left
button3="P9_20" #up
button4="P9_21" #down
pbutton="P9_22" #quit
mbutton="P9_23" #clearscreen

if you want to run the file, be sure to execute it with python3

your specific arguments by the terminal execute are your gridsize.
example:

bone$ python3 Button_Etch.py 15 20 

you grid will get the size x=15 and y=20, be carefull with the x-Value it has to be smaller than the y-Value.

When running use the buttons to walk. With the quit button you can quit the game.
Or use the mbutton to clear the sceen. 

This Etch_sketch is diffrent than the etch_a_sketch from HW01, because the first Etch a sketch 
was done with turtle and couldn't be executed without a display. 
With the normal iot image it wouldn't work. But i proofed the etch_a_sketch with turtle with the exe.windows image. It worked fine!
So it looks like Turtle needs a exe-file.
  
Have fun!

also are some specific gpio measurments through a pdf file acsessable.
They measurement were done with Marius Schwab because during my measurement i ran out of power for my Laptop. 

the question to homework 2 are answered in the question.txt file

========================
Professor Yoder's Comments

Looks good.  ReadME looks complete.  Watch spelling in Questions.txt
The plots are a nice touch.  Make sure you label your axis.
I moved HW02 to hw02....

Score:9/10
