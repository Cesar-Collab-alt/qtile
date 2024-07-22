from libqtile import layout
from libqtile.config import Match

layout_conf = {
    'border_focus':"#ff0000",
    'border_width': 1,
    'margin': 4
}

layouts = [ 
    layout.Columns(**layout_conf),
    layout.Max(),
    layout.MonadTall(**layout_conf),
    # layout.MonadWide(**layout_conf),
    # layout.Bsp(**layout_conf),
    # layout.Matrix(columns=2, **layout_conf),
    # layout.RatioTile(**layout_conf),
   
    # layout.Tile(),
    layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]