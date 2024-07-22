# Multimonitor support
from libqtile.config import Screen
from libqtile import bar
from .widgets import widget_primary , color

def status_bar(widgets):
    return bar.Bar(widgets, 24,margin=4, background=color['bar'][1])

screens = [Screen(top=status_bar(widget_primary ))]
