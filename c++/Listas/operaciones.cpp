#include<iostream>
#include<stdlib.h>
using namespace std;

struct nodo{
	int dato;
	nodo *siguiente;
} *primero, *ultimo;

void insertar();
void imprimir();
void buscar(int dat);
void modificar(int nuevov, int aEliminar);
void eliminar(int del);

int main(){
	
	insertar();
	insertar();
	insertar();
	insertar();
	imprimir();
	buscar(10);
	modificar(1000,20);
	eliminar(30);
	
	return 0;
}

void insertar(){
	nodo *nuevo = new nodo();
	cout<<"Ingrese dato: ";
	cin>>nuevo->dato;
	
	if(primero==NULL){
		primero=nuevo;
		primero->siguiente=NULL;
		ultimo=nuevo;
	}else{
		ultimo->siguiente=nuevo;
		nuevo->siguiente=NULL;
		ultimo=nuevo;
	}
	
	cout<<"Registro guardado"<<endl;
	
}

void imprimir(){
	//[10]->[20]->[30]->NULL
	cout<<"\n\nImprimiendo la lista:"<<endl;
	nodo *actual=new nodo();
	actual=primero;
	
	if(primero!=NULL){
		while(actual!=NULL){
			cout<<" "<<actual->dato;
			actual=actual->siguiente;
		}
	}else{
		cout<<"Lista vacia";
	}
	cout<<endl<<endl;	
}

void buscar(int dat){
	int cont=0, pos=0;
	bool flag;
	//[10]->[20]->[30]->NULL
	cout<<"Buscando dato "<<dat<<endl;
	
	nodo *actual=new nodo();
	actual=primero;
	
	if(primero != NULL){
		while(actual != NULL){
			cont++;
			if(actual->dato==dat){
				actual=actual->siguiente;
				flag=true;
				pos=cont;
				break;
//				cout<<pos<<endl;
			}else{
				actual=actual->siguiente;
				flag=false;
			}
		}
		if(flag){
			cout<<"Encontrado en la pos: ["<<pos<<"]"<<endl;
		}else{
			cout<<"No encontrado"<<endl;
		}
	}else{
		cout<<"Lista vacia";
	}
}


void modificar(int nuevov, int aEliminar){
	int cont=0, pos=0;
	bool flag=false;
	//[10]->[20]->[30]->NULL
	cout<<"\nModificando "<<aEliminar<<" por "<<nuevov<<endl;
	
	nodo *actual=new nodo();
	actual=primero;
	
	if(primero != NULL){
		while(actual != NULL){
			cont++;
			if(actual->dato == aEliminar){
				actual->dato = nuevov;
				flag=true;
				pos=cont;
			}else{
				actual=actual->siguiente;
			}
		}
		if(flag){
			cout<<"Se modifico correctamente"<<endl;
			imprimir();
		}else{
			cout<<"No encontrado"<<endl;
		}
	}else{
		cout<<"Lista vacia";
	}
}

void eliminar(int del){
	bool flag=false;
	cout<<"\nEliminando "<<del<<endl;
	
	nodo *actual=new nodo();
	actual=primero;
	
	if(primero != NULL){
		while(actual != NULL){
			if(actual->dato == del){
				//[10]->[30]->[40]NULL	[10]->[30]->NULL
				actual->dato = actual->siguiente->dato;
				actual->siguiente = actual->siguiente->siguiente;
				flag=true;
			}else{
				actual=actual->siguiente;
			}
		}
		//free(actual);
		if(flag){
			cout<<"Dato eliminado correctamente"<<endl;
			imprimir();
		}else{
			cout<<"No encontrado"<<endl;
		}
	}else{
		cout<<"Lista vacia";
	}
	
}
