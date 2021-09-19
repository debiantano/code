// cadena de caracteres

#include<iostream>
//#include<string.h>

using namespace std;


int main(){
	char palabra[]="cadena de caracteres";
	char palabra2[]={'c','a','d','e','n','a'};
	char nombre[20];
	
	cout<<"Digite su nombre: ";
	cin.getline(nombre,20,'\n');	
	cout<<nombre<<endl;
	
	cout<<palabra<<endl;
	cout<<palabra2<<endl;	
	
	return 0;
}
