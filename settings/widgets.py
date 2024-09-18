from libqtile import widget
from settings.themes_load import cargar_tema
color=cargar_tema()

def render_circle(tipo, color, fondo):
    text = "" if tipo == 1 else ""
    return widget.TextBox(
        fontsize=24,
        background=fondo,
        foreground=color,
        text=text,
        padding=-1,
    )
def render_groups():
    return  widget.GroupBox(
    this_current_screen_border=color['color3'][1],
    active=color['active'][1],
    highlight_method='blok',
    inactive=color['inactive'][1],
    )
widget_primary = [
<<<<<<< HEAD
    render_groups(),
    render_circle(0, color['bar'][1], color['color1'][1]),
    widget.QuickExit(
            default_text='  ',
            countdown_format='[{}]',
            background=color['color1'][1]
        ),
    render_circle(0,color['color1'][1],color['bar'][1]),
        widget.Spacer(),
    render_circle(1,color['color4'][1],color['bar'][1]),
        widget.Clock(
            format="%m/%a %H:%M",
            background= color['color4'][1],
            foreground='#000000',
        ),
    render_circle(0,color['color4'][1],color['bar'][1]),   
=======
     widget.Systray(),
    render_circle(1,color['color3'][1],color['bar'][1]),  
    widget.Memory(
        format="{MemPercent}{ms}%",
        fmt="RAM:{}",
        background=color['color3'][1],
    ),
    render_circle(0,color['color3'][1],color['bar'][1]),  
    widget.Spacer(),
    render_groups(),
>>>>>>> b8a5ca1 (change bar)
    widget.Spacer(),
    widget.Prompt(),
    widget.Chord(
        chords_colors={"launch": ("#ff0000", "#ffffff")},
        name_transform=lambda name: name.upper(),
    ),
<<<<<<< HEAD
    widget.Systray(),
    render_circle(1,color['color3'][1],color['bar'][1]),   
    widget.Memory(
        format="{MemPercent}{ms}%",
        fmt="RAM:{}",
        background=color['color3'][1],
    ),
    render_circle(1,color['color2'][1],color['color3'][1]),
    widget.CurrentLayoutIcon(
        background= color['color2'][1],
        scale=0.65,
    ),  
    render_circle(1,color['color1'][1],color['color2'][1]),
    widget.CheckUpdates(
        background=color['color1'][1],
        colour_have_updates='ffffff',
        colour_no_updates='ffffff',
        display_format='󰚰 : {updates}',
        distro="Arch",
        execute='alacritty -e /usr/bin/pacman -Syu',
        no_update_string='󰟢',
        padding=4,
        update_interval='1800',
    ),
=======
    render_circle(1,color['color2'][1],color['bar'][1]),
    widget.CurrentLayoutIcon(
        background= color['color2'][1],
        scale=0.65,
    ),
    render_circle(0,color['color2'][1],color['bar'][1]),
    render_circle(1,color['color1'][1],color['bar'][1]),
    widget.Clock(
            format="%m/%a %H:%M",
            background= color['color1'][1],
            foreground='#000000',
    ),
    render_circle(0,color['color1'][1],color['bar'][1]),
     render_circle(1, color['color1'][1], color['bar'][1]),
    widget.QuickExit(
            default_text='  ',
            countdown_format='[{}]',
            background=color['color1'][1]
        ),
    render_circle(0,color['color1'][1],color['bar'][1]),
>>>>>>> b8a5ca1 (change bar)
]

widget_secondary = [
    widget.CurrentLayout(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
    foreground=color['light'][1]
)
extension_defaults = widget_defaults.copy()