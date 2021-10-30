#include<iostream>
#include<stdlib.h>

using namespace std;

struct Nodo{
	int dato;
	Nodo *siguiente;
};

void agregarPila(Nodo *&pila, int n);
void quitarPila(Nodo *&pila, int &n);

int main(){
	Nodo *pila=NULL;
	int dato;

	cout<<"Digite dato: ";
	cin>>dato;
	agregarPila(pila,dato);

	cout<<"Digite otro dato: ";
	cin>>dato;

	agregarPila(pila,dato);

	cout<<"\n[!] sacando elementos de la pila"<<endl;

	while(pila != NULL){
		sacarPila(pila,dato);
		if(pila != NULL){
			cout<<dato<<" , ";
		}
		else{
			cout<<dato<<".";
			cout<<endl;
		}
	}


	return 0;
}

void agregarPila(Nodo *&pila, int n){
	Nodo *nuevo_nodo = new Nodo();
	nuevo_nodo->dato = n;
	nuevo_nodo->siguiente = pila;
	pila = nuevo_nodo;

	cout<<"Elemento "<<n<<" agregado a pila"<<endl;
}


//QUITAR PILA
void quitarPila(Nodo*&pila, int &n){
	Nodo *aux=pila;
	n = aux->dato;
	pila = aux->siguiente;
	delete aux;
}


