// Hacer una matriz de tipo entera de 2*2 , llenarla de numeros y luego copiar todo su contenido hacia otra matriz

#include<iostream>
using namespace std;

int main(){
	int matriz[2][2]={{1,2},{3,4}}, copia[2][2];
	
	// pasando el contenido hacia otra matriz
	for(int i=0;i<2;i++){
		for(int j=0;j<2;j++){
			copia[i][j]=matriz[i][j];
		}
	}
	
	cout<<"MOSTRANDO MATRIZ COPIA"<<endl;
	for(int i=0;i<2;i++){
		for(int j=0;j<2;j++){
			cout<<copia[i][j]<<"  ";
		}
		cout<<endl;
	}
	
	
	return 0;
}
