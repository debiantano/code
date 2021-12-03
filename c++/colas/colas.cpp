#include <iostream>
using namespace std;

struct nodo{
	int dato;
	struct nodo *sgte;
};

// Definiendo un tipo de dato tipo struct nodo 
typedef struct nodo *TpNodo;

TpNodo CrearNodo(){
		TpNodo nuevo = new(struct nodo);
		cout<<"Ingrese valor > ";
		cin>>nuevo->dato;
		cout<<endl;
		nuevo->sgte=NULL;
		return nuevo;
}


void Encolar(TpNodo &lista){
	TpNodo p=lista, q = CrearNodo();
	if(lista==NULL){
		lista=q;	
	}
	else{
		while(p->sgte != NULL){
			p=p->sgte;			
		}
		p->sgte=q;	
	}   
}

void menu(){
	system("cls");
	cout<<endl;
	cout<<"1.- ENCOLAR Nodo "<<endl;
	cout<<"2.- DESENCOLAR Nodo "<<endl;
	cout<<"3.- MOSTRAR la cola "<<endl;
	cout<<"0.- Salir"<<endl;
	cout<<"\nOpcion > ";
}

// DESENCOLAR COLA
void Desencolar(TpNodo &lista){
 	TpNodo t=lista;
 	lista=lista->sgte;
 	cout<<"\nNodo eliminado Nr. " <<t->dato<<endl<<endl;
 	delete(t);
 	
 }

// MOSTRAR COLA
void mostrar(TpNodo &lista){
	TpNodo temp=lista;
	int n=1;	// contador de nodos
	
	while(temp!=NULL){
		cout<<"Nodo ["<<n<<"] con valor: "<<temp->dato<<endl;
		temp=temp->sgte;
		n++;
	}
}

// FUNCION PRINCIPAL
int main( ) {
	TpNodo t=NULL, lista=NULL, p=NULL, q=NULL;
	int opc, n;
	do{
		menu();
		cin>>opc;
		switch(opc){
			case 1:{
				Encolar(lista);
				break;
			}
			case 2:{
				Desencolar(lista);
				system("pause>nul");
				break;			
			}
			case 3:{
				mostrar(lista);
				system("pause>nul");
				break;
			}	
	
		}		
	}while(opc !=0);
	
	return 0;
}
