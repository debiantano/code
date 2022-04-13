from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os

mod = "mod4"
terminal = "gnome-terminal" #guess_terminal()

# COLORES
bg_general="#474752"




keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # PERSONALIZATION TECLAS
    Key([mod, "shift"], "f", lazy.spawn("firefox"), desc="Launch Firefox"),
    Key([mod], "d", lazy.spawn("rofi -show run"), desc="Launch Rofi"),
]

groups = [Group(i) for i in [
	"  ",
	"  ",
	"  ",
	"  ",
	"  ",
	"  ",
	"  "
]]

for i, group in enumerate(groups):
    numberDesktop = str(i+1)
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                numberDesktop,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                numberDesktop,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.MonadTall(
        border_width=2,
        border_focus="#d70000",
        single_border_width=0, # No enfocar si hay un panel
        margin=10
        # VARS
    )
]

widget_defaults = dict(
    font="Hack Nerd Font",
    fontsize=16,
    padding=0, # 0 para q funcione los bordeados
)
extension_defaults = widget_defaults.copy()

def ip():
    ip=os.popen('echo $(ip addr | grep -oP "192.168.100.\\d\\d" | head -n 1)').read().rstrip("\n")
    return ip

def HackTheBox():
    htb=os.popen('echo $(ip addr | grep tun0 -B3 | tail -n 1 | xargs | awk \'{print $2}\' | cut -d \"/\" -f 1)').read().rstrip("\n")
    if htb != None:
        return htb
    else:
        t="No target"
        return t

screens = [
    Screen(
        top=bar.Bar( # top arriba
            [
                #widget.CurrentLayout(),
                widget.GroupBox(
                    active="#ffffff", # esc. activo
                    inactive="#8fa0cd", # esc inactivos
                    highlight_method="block", # esc. ocupado
                    other_screen_border="#6d046c", # border del esc.
                    background="#000000", # fondo total de esc.
#                    foreground="#f306f0",
                    borderwidth=0, # borde
                    fontsize=17,	# tamaño de los iconos
                    this_current_screen_border=bg_general, # color dentro del esc.
                    urgent_alert_method="block",
                    urgent_border="#a70000",
                    padding_x=3,
                    padding_y=0
                ),
                widget.TextBox( # IP CONFIG      ﲕ   
                    text="◤",
                    fontsize=60,
                    foreground="#000000",
                    background=bg_general
                ),
                widget.Sep( # separacion
                    linewidth=0,
                    padding=600,
#                    foreground="#8fa0cd",
                    background=bg_general
                ),
#                widget.QuickExit(),		  
#################################################
                 widget.TextBox( # IP CONFIG ◢■■■■■■■◤
                     text="◢",
                     fontsize=60,
                     foreground="#000000",
                     background=bg_general
                 ),
                 widget.TextBox(
                     text="  ",
                     fontsize=16,
                     foreground="#ff57b5",
                     background="#000000"
                 ),
                 widget.GenPollText(
                     background="#000000",
                     func=ip,
                     update_interval=20,
                     foreground="#ffffff",
                     font="sans"
                 ),
                 widget.TextBox( # IP CONFIG      ﲕ   
                     text="◤",
                     fontsize=60,
                     foreground="#000000",
                     background=bg_general
                 ),
                 widget.TextBox(
                     text="  ",
                     fontsize=20,
                     foreground="#3aff00",
                     background=bg_general
                 ),
                 widget.GenPollText(
                     background=bg_general,
                     func=HackTheBox,
                     update_interval=2,
                     foreground="#ffffff",
                     font="sans"
                 ),
                 widget.TextBox(
                     text="◢",
                     fontsize=60,
                     foreground="#000000",
                 ),
                 widget.Clock(
                     background="#000000",
                     font="Hack Nerd Font",
                     format="%H:%M"
                 ),
                 widget.TextBox(
                     text="◤",
                     fontsize=60,
                     foreground="#000000",
                 ),
                 widget.TextBox(
                     text="  ",
                     foreground="#01d1b4",
                     fontsize=20
                 ),
                 widget.TextBox(
                     text="◢",
                     fontsize=60,
                     foreground="#000000"
                 ),
                 widget.Sep(
                 background="#000000",
                 foreground="#000000",
                 linewidth=100
                 )

            ],
            24,
            background=bg_general, # barra total
            margin=[9,9,0,9]
#            border_width=[5, 5, 5, 5],  # Draw top and bottom borders
#            border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

cmd = [
	"setxkbmap latam",
	"feh --bg-fill /home/noroot/Images/wallpaper.jpg"
]

for x in cmd:
	os.system(x)
