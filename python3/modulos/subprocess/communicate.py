# Almacenar la salida y los mensajes de error en una cadena

import subprocess
from subprocess import Popen

p=Popen(["ls", "qw"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
output, errors= p.communicate()

#print(output)
#print(errors)
