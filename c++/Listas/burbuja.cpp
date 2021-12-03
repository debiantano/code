#include <iostream>

using namespace std;

struct nodo{
	int dato;
	struct nodo *sgte;
};

int nrnodos=0;
// Definiendo un tipo de dato tipo struct nodo 
typedef struct nodo *TpNodo;

TpNodo CrearNodo(){
		TpNodo nuevo = new(struct nodo);
		cout<<"Ingresar valor > ";
		cin>>nuevo->dato;
		cout<<endl;
		nuevo->sgte=NULL;
		return nuevo;
}

// INSERTAR NODO AL FINAL
void InsertarFinal(TpNodo &lista){
	TpNodo p=lista, q = CrearNodo();
	if(lista==NULL)
	   lista=q;
	else{
		while(p->sgte != NULL)
			p=p->sgte;
		p->sgte=q;	
	}   
}

// MENU 
void menu(){
	system("cls");
	cout<<endl;
	cout<<"1.- INSERTAR nodo"<<endl;
	cout<<"2.- MOSTRAR elementos"<<endl;
	cout<<"3.- Ordenamiento burbuja"<<endl;	
	cout<<"0.- Salir"<<endl;
	cout<<"\nOpcion > ";
}

// ORDENAMIENTO METODO BURBUJA
void Burbuja(TpNodo &lista){
 	TpNodo p=lista;
 	int t=0, n=0;
 	bool flag=true;
 	
 	if(lista ==NULL){
 		cout<<"Lista Vacia...."<<endl;
 		system("pause");
 		return;
 	 }
 	
 	// Contar los nodos de la lista
     while(p != NULL){
     		n++;
     		p=p->sgte;
	 } 
	 
	 for(int i=0; (i<n-1 && flag==true) ;i++ ){
	 	p=lista;
	 	flag=false;
	 
	  while(p->sgte != NULL){
	  		cout<<"pasada" << i+1<<" compara "<<p->dato<<" con "<<p->sgte->dato<<endl;
	  		if(p->dato > p->sgte->dato)	{
	  			t=p->dato;
	  			p->dato=p->sgte->dato;
	  			p->sgte->dato=t;
	  			flag=true;
	  		 }//if
	  		p=p->sgte;	
	  }//while
	 
	 }// for
	cout<<"Lista se ordeno exitosamente .... "<<endl;
	system("pause>nul");		 		
 }
 
// MAIN
int main(){
	TpNodo t=NULL, lista=NULL, p=NULL, q=NULL;
	int opc, n;
	do{
		menu();
		cin>>opc;
		
		switch(opc){
			
			case 1:{
				InsertarFinal(lista);
				break;
			}
			
			case 2:{
				p=lista;
				n=1;
				while(p!=NULL){
					cout<<"Nodo ["<<n<<"] con valor : "<<p->dato<<endl;
					p=p->sgte;
					n++;
				}
				system("pause>nul");
				
				break;
			}
			
			case 3:{
				Burbuja(lista);	
				break;
				}
		}		
	}while(opc !=0);
	
	return 0;
}
