# Here's how to use imagemagick to display text
# Make a blank image
SIZE=240x320
TMP_FILE=/tmp/frame.png

# From: http://www.imagemagick.org/Usage/text/
convert -background lightblue -fill blue -font Times-Roman -pointsize 30 \
      -size $SIZE \
      label:'\Vinzenz Felder' \
      -draw "text 0 ,100 'PIZZA'" \
      $TMP_FILE

sudo fbi -e -noverbose -T 1 -a $TMP_FILE

# convert -list font
