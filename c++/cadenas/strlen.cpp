// Funcion strlen
#include<iostream>
#include<string.h>
#define N 3
using namespace std;

int main(){
	char cadena[20];
	
	cout<<"Digite una cadena: ";
	cin.getline(cadena,20,'\n');
	
	cout<<"Longitud: "<<strlen(cadena)<<endl;

	return 0;
}
