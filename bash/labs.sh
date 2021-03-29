
set force_conservative 1  ; # set to 1 to force conservative mode
if {$force_conservative} {
        set send_slow {1 .1}
        proc send {ignore arg} {
                sleep .1
                exp_send -s -- $arg
        }
}

set timeout -1
spawn openvpn OS-XXXXXX-PWK.ovpn
match_max 100000
expect "Enter Auth Username: "
send -- "[USERNAME]\r"
expect -exact "Enter Auth Password: (press TAB for no echo) "
send -- "[PASSWORD]\r"

# Ensure that control-C is sent to openvpn when the user wants
trap {
    send -- "^C"
} SIGINT

expect eof
