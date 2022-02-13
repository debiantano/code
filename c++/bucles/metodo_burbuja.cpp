// Ordenamiento por el metodo burbuja

#include<iostream>
using namespace std;

int main(){
	int numeros[5];
	int i,j,aux;
	
	for(i=0;i<5;i++){
		cout<<"Digite un numero: ";
		cin>>numeros[i];
	}
	
	//Metodo burbuja
	for(i=0;i<5;i++){
		for(j=0;j<4;j++){
			if(numeros[j]>numeros[j+1]){
				aux=numeros[j];
				numeros[j]=numeros[j+1]; 
				numeros[j+1]=aux;
			}
		}
	}
	
	for(i=0;i<5;i++){
		cout<<numeros[i]<<endl;
	}
	
	
	return 0;
}
