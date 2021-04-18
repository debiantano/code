# Explotando el Buffer Overflow basado en pila (linux)

- [Antecedentes](#Antecedente)
- [Creacion del script en C](#creando-script-en-c)

#include<stdio.h>

void secretFunction(){
        printf("[+] Congratulations!\n");
        printf("Has entrado a la funcion secreta");
}

void echo(){
        char buffer[20];
        printf("Enter some text: ");
        scanf("%s", buffer);

        printf(">> %s", buffer);
}

int main(){
        echo();
        return 0;
}



#include<stdio.h>

void secretFunction(){
        printf("[+] Congratulations!\n");
        printf("Has entrado a la funcion secreta");
}

void echo(){
        char buffer[20];
        printf("Enter some text: ");
        scanf("%s", buffer);

        printf(">> %s", buffer);
}

int main(){
        echo();
        return 0;
}


#include<stdio.h>

void secretFunction(){
        printf("[+] Congratulations!\n");
        printf("Has entrado a la funcion secreta");
}

void echo(){
        char buffer[20];
        printf("Enter some text: ");
        scanf("%s", buffer);

        printf(">> %s", buffer);
}

int main(){
        echo();
        return 0;
}





Antecedentes
==========================
asdfgh
sdfgh
sdfgh

Creando script en C
sdfg
wert
sdfg
rty
rt
