#!/bin/bash

# Terminate already running picom instances
killall picom

# Launch picom with experimental backend for double kua something usingt config location ~/.config/picom/picom.conf
picom --experimental-backends 2>&1 | tee -a /tmp/picom.log & disown

echo "Picom launched..."
