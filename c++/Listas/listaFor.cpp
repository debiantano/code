#include<iostream>
#include<conio.h>

using namespace std;

struct Nodo{
	int dato;
	Nodo *siguiente;
};

void insertarDato(Nodo *&,int);
void mostrarLista(Nodo *);

int main(){

	Nodo *lista=NULL;
	int dat;

	for(int i=0;i<5;i++){
		cout<<"Ingresa dato> ";
		cin>>dat;
		insertarDato(lista,dat);
	}

	mostrarLista(lista);

}

void insertarDato(Nodo *&lista,int dat){
	Nodo *nuevo_dato = new Nodo();
	Nodo *aux;
	
	nuevo_dato->dato=dat;
	nuevo_dato->siguiente;
	
	if(lista == NULL){
		lista=nuevo_dato;
	}else{
		aux=lista;
		while(aux->siguiente != NULL){
			aux=aux->siguiente;
		}
		aux->siguiente=nuevo_dato;
	}
	
}

void mostrarLista(Nodo *lista){
	while(lista != NULL){
		cout<<lista->dato<<"  ";
		lista=lista->siguiente;
	}
}
