// Metodo por seleccion

#include<iostream>
#define MAX 5

using namespace std;

int main(){
	int numeros[MAX];
	int i, j, aux, min;
	
	for(i=0;i<MAX;i++){
		cout<<"Digite un numero: ";
		cin>>numeros[i];
	}
	
	// Seleccion
	for(i=0;i<MAX;i++){
		min=i;
		for(j=i+1;j<MAX;j++){
			if(numeros[j]<numeros[i]){
				min=j;
			}
		}
		aux=numeros[i];
		numeros[min]=aux;
	}
	
	cout<<"\nOrden Descendente:"<<endl;
	for(i=MAX-1;i>=0;i--){
		cout<<numeros[i]<<endl;
	}
	
	return 0;
}
