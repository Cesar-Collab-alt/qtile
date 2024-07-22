#!/bin/sh

# Restaurar fondo de pantalla
pgrep -x nitrogen || nitrogen --restore &

# Iniciar udiskie para manejo de dispositivos
pgrep -x udiskie || udiskie -t &

# Iniciar el applet de Network Manager
pgrep -x nm-applet || nm-applet &

# Iniciar el compositor picom
pgrep -x picom || picom &

# Iniciar el applet de PulseAudio
pgrep -x pa-applet || pa-applet &

