#The files to look at for this homework assignment are the beaglebone memorymap pdf, GPIO_button_mmap.c, gpio_toggle.c, and and the directory with all sh.files for testing LCD

#The beaglebone memory map is for the first homework section and is a system memory map of the AM335x showing things such as the addresses and size for EMIF0 SDRAM and the GPIO registers.

#The GPIO_button_mmap.c is a c script the makes use of the mmap function. This script maps to two GPIO registers, GPIO1 and GPIO3. It uses two buttons connected to the GPIO P9_25 and GPIO P9_23 to control two of the internal LEDs on the beagleboard(execute ./GPIO_button.mmap)

#The gpio_toggle.c is a file wich toggles on internal LED 

#The gpioThru script was modified to read from a switch connected to GPIO1_25 and use it to control an internal LED.

#in the directory display, you will find all the files for the Display

#I edited the rotate command in 'reset.sh' and 'on.sh' so that the display would rotate an image or video 90 degrees.

#boris.sh will display boris the beagle on the display, by full screen.(See boris2.jpg in images)If it is not working execute it via sudo

#text.sh uses Imagemagick to print my name and a message on a white screen(see Text2.jpg in images)

#movie.sh shows a movie on the Display, by changing the quote "rotate" you can rotate the video. 

#I have not used pygame before so I did not run this on the display

#install.sh is install file to install all necessary packages for the display

#off.sh can be executed to shut off the LCD.





