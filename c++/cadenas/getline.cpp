// cadena de caracteres con getline

#include<iostream>
//#include<string.h>

using namespace std;


int main(){
	string cadena1;
	
	cout<<"Introduce una cadena: ";
	getline(cin,cadena1);
	
	cout<<"La cadena es: "<<cadena1;
	
	return 0;
}
