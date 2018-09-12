Hello, 

here is the HW2 for Linux 32-Embedded Class. 

In the directory you can find a file LED_Button.py , 
to toggle LED's via buttons make sure you connected to the right pins.

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
 
Have fun!

also are some specific gpio measurments through a pdf file acsessable.
They measurement were done with Marius Schwab because during my measurement i ran out of power for my Laptop. 

the question to homework 2 are answered in the question.txt file
