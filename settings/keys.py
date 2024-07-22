from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
   # Open code
    Key([mod], "c", lazy.spawn("code"), desc="Open new browser tab"),
    # Show file manager
    Key([mod], "e", lazy.spawn("pcmanfm"), desc="Open new browser window"),
    # Show menu
    Key([mod], "m", lazy.spawn("bash /home/cesar/.config/rofi/launchers/type-7/launcher.sh"), desc="Abrir menu"),
    # Switch between windows
    Key([mod], "a", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "d", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "s", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "w", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "a", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "d", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "s", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "w", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "x", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Comando para apagar
    Key([], "F4", lazy.spawn("poweroff"), desc="Power off desktop"),
    # Controles de volumen
    Key(["control"], "F1", lazy.spawn("pulsemixer --id sink-0 --change-volume -10"), desc="Volume down"),
    Key(["control"], "F2", lazy.spawn("pulsemixer --id sink-0 --change-volume 10"), desc="Volume up"),
    # Capturas de pantalla (usando scrot)
    Key([mod], "s", lazy.spawn("scrot /home/cesar/capturas/'%Y-%m-%d-%H-%M-%S_$wx$h.png'"), desc="Screenshot complete"),
    Key([mod, "shift"], "s", lazy.spawn("scrot -l style=dash,width=3,color='red' -s /home/cesar/capturas/'%Y-%m-%d-%H-%M-%S_$wx$h.png'"), desc="Screenshot selection"),
]