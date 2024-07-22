import subprocess
from libqtile import hook

from settings.themes_load import os
from settings.keys import keys, mod, terminal
from settings.groups import groups, group
from settings.widgets import extension_defaults
from settings.layouts import layouts
from settings.myScreens import screens
from settings.myMouse import mouse       

def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])

@hook.subscribe.startup_once
def start_once():
    autostart()

main = None
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = 'urgent'
wmname = 'LG3D'
