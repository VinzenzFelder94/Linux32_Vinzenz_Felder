# The main files for HW03 are temp.sh, i2c_temp.py, Display_Etch.py, Display_Etch_button.py

# temp.sh is a shell program that reads out the values of two TMP101 sensors connected to the i2c bus in Fahrenheit.

# i2c_temp.py reads pins of the TMP101 sensors and shows the tempurature of both sensors.

# a jpg.file is attached to show the wiring of the temperatur sensors

# Display_Etch_button.py connects the previously made in hw02 etch a sketch with buttons to output to the led matrix. The pins are now diffrent than bevor. Pinning is printed below.
  
  # button1="P9_23" #Right P9_pins and 2 user buttons used
  # button2="P9_24" #left
  # button3="P9_25" #up
  # button4="P9_26" #down
  # pbutton="P9_21" #quit
  # mbutton="P9_22" #clear screen



# Display_Etch_button.py is a update of Display_Etch_button.py by controling the EtchaSketch program by encoders. 
  the quit and clear screen buttons are still the same than from the previous 
  the ecoders are running with eQEP. make sure to execute the setup.sh in ~/exercises/sensors/eQEP otherwise the second encoder will not work. 
  Pinning from the encoder are:

   P8_33, P8_35 for eQEP1
   P8_41, P8_42 for eQEP2

========================
Professor Yoder's Comments

Looks good.  The wiring .pjg is a nice touch.

Score:10/10