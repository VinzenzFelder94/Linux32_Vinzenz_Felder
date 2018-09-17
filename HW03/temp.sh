#!/bin/bash
for((;;))
#main loop
do
  # get temp values
  temp1=`i2cget -y 2 0x48`
  temp2=`i2cget -y 2 0x49`

  tempF1=$((($temp1*9/5)+32)) # convert temp1 to Fahrenheit

  tempF2=$((($temp2*9/5)+32)) # convert temp2 to Fahrenheit
  # output to console
  echo Sensor1 $tempF1 and Sensor2 $tempF2 degrees Fahrenheit
  sleep 1
done




