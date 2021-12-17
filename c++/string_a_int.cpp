#include <iostream>
#include <cstdlib>
 
using namespace std;
/*
* Programa que convierte una cadena a un entero int y le suma 2
*/
 
int main ()
{
    //Declaracion de variables en string
    string numero;
    //pide y guarda los valores en numero
    cout << "¿cual es el numero?" << endl;
    cin >> numero;
 
    //convierte tu cadena a un entero le suma 2 y te muestra el resultado
    cout << "Tu numero es " <<  atoi(numero.c_str())+2;
    return 0;
}
