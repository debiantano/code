
#include<iostream>
#include<string.h>

using namespace std;

void cuadrado(int vector[], int TAM){
	for(int i=0;i<TAM;i++){
		vector[i]*=vector[i];
	}
}

void mostrar_vector(int vector[], int TAM){
	for(int i=0;i<TAM;i++){
		cout<<vector[i]<<"  ";
	}
}

int main(){
	const int TAM=5;
	int vector[TAM]={1,2,3,4,5};
	
	cuadrado(vector, TAM);
	mostrar_vector(vector, TAM);
	
	return 0;
}
