#!/bin/sh
# From: https://gist.github.com/jadonk/0e4a190fc01dc5723d1f183737af1d83

export FRAMEBUFFER=/dev/fb0


# Play a movie
SDL_VIDEODRIVER=fbcon 
SDL_FBDEV=/dev/fb0
mplayer -vf-add rotate=4 -framedrop ./images/RedsNightmare.mpg

# Look at the framebuffer settings
fbset
