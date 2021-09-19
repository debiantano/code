from colorama import init, Fore

init()
class color:
        red = Fore.RED
        blue = Fore.BLUE
        green = Fore.GREEN
        yellow = Fore.YELLOW
        error = Fore.RED+"["+Fore.RESET+"-"+Fore.RED+"]"+Fore.RESET+" "
        adv = Fore.YELLOW+"["+Fore.RESET+"!"+Fore.YELLOW+"]"+Fore.RESET+" "
        ble = Fore.BLUE+"["+Fore.RESET+"*"+Fore.BLUE+"]"+Fore.RESET+" "
        reset = Fore.RESET

print(color.red + "Esto es amarillo" + color.reset)
print(color.blue + "Esto es azul" + color.reset)
print(color.green + "Esto es verde" + color.reset)
print(color.yellow + "Esto es amarillo" + color.reset)
print(color.error + "Esto es un error" + color.reset)
print(color.adv + "Esto es una advertencia" + color.reset)
print(color.ble + "Esto es un success" + color.reset)
