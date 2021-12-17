#include<iostream>
#include<string.h>
#include<fstream>
//#include<conio.h>
//#include<stdio.h>

using namespace std;

struct nodo{
	char id[10], nombre[20], precio[10], cantidad[10];
	nodo *sgte;	
};

typedef struct nodo *TpNodo;
TpNodo lista=NULL,primero=NULL;

void carga_archivo(){
	char id[10], nombre[20], precio[10], cantidad[10];
	ifstream arch;
	arch.open("productos.txt", ios::in);
	
	while(!arch.eof()){
		arch >>id >>nombre >>precio >>cantidad;
		
		if(!arch.eof()){
			TpNodo nuevo = new(struct nodo);
			strcpy(nuevo->id,id);
			strcpy(nuevo->nombre,nombre);
			strcpy(nuevo->precio,precio);
			strcpy(nuevo->cantidad,cantidad);
			if(primero==NULL){
				primero=nuevo;
				primero->sgte=NULL;
				lista=primero;
			}else{
				lista->sgte=nuevo;
				nuevo->sgte=NULL;
				lista=nuevo;
			}
		}
	}
	arch.close();
}

void mostrar(){
	TpNodo actual=primero;
	while(actual != NULL){
		cout<<"\t\t"<<actual->id<<"\t\t"<<actual->nombre<<"\t\t"<<actual->precio<<"\t\t"<<actual->cantidad<<endl;
		actual=actual->sgte;
	}
}


int main(){
	carga_archivo();
	mostrar();
	
	return 0;
}
