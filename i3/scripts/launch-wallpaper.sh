#!/bin/bash

WALLPAPER_GIF="$HOME/.config/i3/gifs/01.gif"

# Terminate already running gifview/xwinwrap instances
killall gifview

xwinwrap -g 1920x1080 -ov -ni -s -nf -- gifview -w WID $WALLPAPER_GIF -a

echo "Gif wallpaper launched..."
