/*
Hacer un programa que permita ordenar alfabéticamente una lista de nombres de tamaño N considerado 
constante. El tamaño máximo de las cadenas es 20. 
*/

#include<iostream>
#include<string.h>
#define N 5
using namespace std;

int main(){
	char nombre[N][20];
	char aux[20];
	int i,j;
	
	// LLenando datos
	for(i=0;i<N;i++){
		cout<<"["<<i<<"] "<<"Introduce un nombre: ";
		cin>>nombre[i];
		
		if(strlen(nombre[i])>20){
			cout<<"[!] Nombre no admitido"<<endl;
		}
	}
		
	for(i=0;i<N-1;i++){
		for(j=i+1;j<N;j++){
			if(strcmp(nombre[i],nombre[j])>0){
				strcpy(aux,nombre[i]);
				strcpy(nombre[i], nombre[j]);
				strcpy(nombre[j], aux);
			}
		}
	}

	for(i=0;i<N;i++){
		cout<<endl<<nombre[i];
		
	}

	return 0;
}
