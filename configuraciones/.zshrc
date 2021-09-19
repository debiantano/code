#source ~/powerlevel10k/powerlevel10k.zsh-theme
source /home/noroot/km4l30n/tools/powerlevel10k/powerlevel10k.zsh-theme

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
#[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

#PATH
PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/usr/local/go/bin:/home/noroot/.local/bin

#export PATH=$PATH:/usr/local/go/bin

# Fix the Java Problem
export _JAVA_AWT_WM_NONREPARENTING=1

# Keep 1000 lines of history within the shell and save it to ~/.zsh_history:
HISTSIZE=10000
SAVEHIST=10000
HISTFILE=~/.zsh_history


function mkt(){
	mkdir {enumeration,Exploitation,PrivEsc}
	echo -e "ENUMERACION\n\nEXPLOTACION\n\nESCALADA DE PRIVILEGIOS\n\nFLAGS\n\n" > credential.txt
}


alias interactiveShell='python /home/noroot/km4l30n/python_scripting/interactiveShell.py'
alias cat='/usr/bin/bat'
alias catn='/usr/bin/cat'
alias ls='/usr/bin/lsd'
alias burpPro='pushd /home/noroot/Escritorio/burpSuite\ Professional && /usr/lib/jvm/java-11-openjdk-amd64/bin/java --illegal-access=permit -Dfile.encoding=utf-8 -javaagent:BurpSuiteLoader_v2020.7.jar -noverify -jar burpsuite_pro_v2020.7.jar >/dev/null 2>&1 &; popd'


# Set 'man' colors
function man() {
    env \
    LESS_TERMCAP_mb=$'\e[01;31m' \
    LESS_TERMCAP_md=$'\e[01;31m' \
    LESS_TERMCAP_me=$'\e[0m' \
    LESS_TERMCAP_se=$'\e[0m' \
    LESS_TERMCAP_so=$'\e[01;44;33m' \
    LESS_TERMCAP_ue=$'\e[0m' \
    LESS_TERMCAP_us=$'\e[01;32m' \
    man "$@"
}

function monitorInit(){
	airmong-ng start wlan0 > /dev/null 2>&1
	killall dhclient wpa_supplicant 2>/dev/null
	ifconfig wlan0mon down
	macchanger -a > /dev/null 2>&1
	ifconfig wlan0mon up
}

# Extract nmap information

function extractPorts(){
	ports="$(/usr/bin/cat $1 | grep -oP '\d{1,5}/open' | awk '{print $1}' FS='/' | xargs | tr ' ' ',')"
	ip_address="$(cat $1 | grep -oP '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' | sort -u | head -n 1)"
	echo -e "\n[*] Extracting information...\n" > extractPorts.tmp
	echo -e "\t[*] IP Address: $ip_address"  >> extractPorts.tmp
	echo -e "\t[*] Open ports: $ports\n"  >> extractPorts.tmp
	echo $ports | tr -d '\n' | xclip -sel clip
	echo -e "[*] Ports copied to clipboard\n"  >> extractPorts.tmp
	cat extractPorts.tmp; rm extractPorts.tmp
}

source /usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
#[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
