'''
> nano /usr/share/xession/qtile.desktop
[Desktop Entry]
Name=Qtile
Comment=Qtile Session
Exec=qtile start
Type=Application
Keywords=wm;tiling
'''
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os 

mod = "mod4"
terminal = "gnome-terminal"

# COLORES
bg_general="#474752"

keys = [
    # Cambiar entre ventanas
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),

    # Mover ventanas entre las columnas izquierda/derecha o subir/bajar en la pila actual.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Crecer ventanas
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),

    # ATAJOS
    # abrir terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # matar una ventana
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    # recargar conf de qtile
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    # cerrar sesion
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # PERSONALIZATION TECLAS
    # abrir firefox
    Key([mod, "shift"], "f", lazy.spawn("firefox"), desc="Launch Firefox"),
    # abrir burpsuite
    Key([mod, "shift"], "b", lazy.spawn("burp-StartBurp"), desc="Launch BurpSuite"),
    # lanzar rofi
    Key([mod], "d", lazy.spawn("rofi -show run"), desc="Launch Rofi"),
    # desactivar modo flotante
    Key([mod], "f", lazy.window.toggle_floating(), desc="mode floating disable"),
    # Screenshot en clipboard
    Key([mod, "shift"], "Print", lazy.spawn("scrot \"test.png\" -s -e 'xclip -selection clipboard -t image/png -i $f && rm test.png'")),
    # Screenshot guardado en dir. actual
    Key([mod], "Print", lazy.spawn("scrot archLinux-%d-%H-%S.png -e 'mv *.png /home/noroot/Images/screenShots'")),
    # Mostrar IP
    Key([mod], "i", lazy.spawn('bash -c \"zenity --info --text=$(/usr/bin/cat /home/noroot/.config/qtile/ip_machine.txt) --ok-label=\"ok\" 2>/dev/null\"'))
]

# PROGRAMAS EN DETERMINADO WORKSPACE
groups = [
	Group("  "),
	Group("  ", matches=[Match(wm_class=["Navigator"])]),
	Group("  ", matches=[Match(wm_class=["burp-StartBurp","cherrytree", "code-oss"])]),
	Group("  ", matches=[Match(wm_class=["Thunar"])]),
	Group("  "),
	Group("  "),
	Group("  "),
	Group("  ")
]

for i, group in enumerate(groups):
    numberDesktop = str(i+1)
    keys.extend(
        [
           # cambiar a grupo
            Key([mod], numberDesktop, lazy.group[group.name].toscreen(), desc="Switch to group {}".format(group.name)),
            # mover ventana enfocada a un grupo
            Key([mod, "shift"], numberDesktop, lazy.window.togroup(group.name, switch_group=True), desc="Switch to & move focused window to group {}".format(group.name)),
        ]
    )

layouts = [
     layout.Columns(
         border_focus="#d70000",
#         single_border_width=0, # no enfocar si hay un panel
         margin_on_single=10,
         border_width=2,	# grosor del contorno
         margin=5)	# size gaps
]

# BAR QTILE CONF
widget_defaults = dict(
    font="Hack Nerd Font",
    fontsize=16,
    padding=0, # 0 para q funcione los bordeados
)
extension_defaults = widget_defaults.copy()

# FUNCION OBETENER IP
def ip():
    ip=os.popen('echo $(ip addr | grep -oP "192.168.100.\\d\\d" | head -n 1)').read().rstrip("\n")
    if ip != None:
        return ip
    else:
        return None

# VPN HACKTHEBOX
def HackTheBox():
    htb=os.popen('echo $(ip addr | grep tun0 -B3 | tail -n 1 | xargs | awk \'{print $2}\' | cut -d \"/\" -f 1)').read().rstrip("\n")
    if htb != None:
        return htb
    else:
        t="No target"
        return None

###########################################################################################################################
screens = [
    Screen(
        top=bar.Bar( # top arriba
            [
                widget.GroupBox(
                    active="#ffffff", # esc. activo
                    inactive="#8fa0cd", # esc inactivos
                    highlight_method="block", # esc. ocupado
                    other_screen_border="#6d046c", # border del esc.
                    background="#000000", # fondo total de esc.
                    borderwidth=0, # borde
                    fontsize=17,	# tamaño de los iconos
                    this_current_screen_border=bg_general, # color dentro del esc.
                    urgent_alert_method="block",
                    urgent_border="#a70000",
                    padding_x=3,
                    padding_y=0
                ),
                
                widget.TextBox(
                    text="◤",
                    fontsize=60,
                    foreground="#000000",
                    background=bg_general
                ),
                
                widget.Sep( # separacion
                    linewidth=0,
                    padding=570,
                    background=bg_general
                ),
                
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
                 
                 widget.TextBox(
                     text="◤",
                     fontsize=60,
                     foreground="#000000",
                     background=bg_general
                 ),
                 
                 widget.TextBox( # HTB
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
                 linewidth=200
                 )
            ],
            24,
            background=bg_general, # barra total
            margin=[9,9,0,9]
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()), # click izquierdo
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),	# click derecho
]

###dgroups_key_binder = None
###dgroups_app_rules = []  # type: list

# No enfocar con el mouse
follow_mouse_focus = False
# No llevar atras al flotante
bring_front_click = False

# ABRIR MODO FLOTANTE
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="burp-StartBurp"),  # xprop WM_CLASS
        Match(wm_class="feh"),
        Match(wm_class="tk"),
        Match(wm_class="zenity")
    ]
)

###auto_fullscreen = True
###focus_on_window_activation = "smart"
###reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
#auto_minimize = True

### When using the Wayland backend, this can be used to configure input devices.
###wl_input_rules = None

# java that happens to be on java's whitelist.
wmname = "LG3D"

# EJECUTAR AL INICIO
cmd = [
	"setxkbmap latam",
	"feh --bg-fill /home/noroot/Images/wallpaper.jpg"
]

for x in cmd:
	os.system(x)
