#include<iostream>
#include<stdlib.h>

using namespace std;

struct Nodo{
	int dato;
	Nodo *siguiente;
};

void agregarPila(Nodo *&pila, int n);


int main(){
	Nodo *pila=NULL;
	int n1,n2;

	cout<<"Digite dato: ";
	cin>>n1;
	agregarPila(pila,n1);

	cout<<"Digite otro dato: ";
	cin>>n2;

	agregarPila(pila,n2);

	return 0;
}

void agregarPila(Nodo *&pila, int n){
	Nodo *nuevo_nodo = new Nodo();
	nuevo_nodo->dato = n;
	nuevo_nodo->siguiente = pila;
	pila = nuevo_nodo;

	cout<<"Elemento "<<n<<" agregado a pila"<<endl;
}
