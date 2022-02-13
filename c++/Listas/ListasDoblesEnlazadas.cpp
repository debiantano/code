#include<iostream>
#include<conio.h>
#include<windows.h>
using namespace std;

struct nodo{
	int dato;
	struct nodo *sgte;
	struct nodo *ant;
};

enum Colors {
	BLACK = 0,
	BLUE = 1,
	GREEN = 2,
	CYAN = 3,
	RED = 4,
	MAGENTA = 5,
	BROWN = 6,
	LGREY = 7,
	DGREY = 8,
	LBLUE = 9,
	LGREEN = 10,
	LCYAN = 11,
	LRED = 12,
	LMAGENTA = 13,
	YELLOW = 14,
	WHITE = 15
};

typedef struct nodo *TpNodo;

// COLORES
void Color(int Background, int Text){
	HANDLE Console = GetStdHandle(STD_OUTPUT_HANDLE); // Tomamos la consola.
	int color_nuevo= Text + (Background * 16);
	SetConsoleTextAttribute(Console, color_nuevo); // Guardamos los cambios en la Consola.
}


// CREAR NODO
TpNodo CrearNodo(){
		TpNodo nuevo = new(struct nodo);
		cout<<"Ingresar valor > ";cin>>nuevo->dato;
		cout<<endl;
		nuevo->sgte=NULL;
		nuevo->ant=NULL;
		return nuevo;
}


// INSERTAR NODO AL INICIO
void InsertarInicio(TpNodo &lista){
	TpNodo  q = CrearNodo();
	if(lista!=NULL){
		q->sgte=lista;
		lista->ant = q;
	}
	lista=q;
}

// INSERTAR NODO AL FINAL
void InsertarFinal(TpNodo &lista){
	TpNodo temp=lista, q = CrearNodo();
	if(lista==NULL){
		lista=q;
	}
	else{
		while(temp->sgte != NULL){
			temp=temp->sgte;
		}
		temp->sgte=q;
		q->ant=temp;	
	}   
}


// INSERTAR NODO POR POSICION
void InsertarPosicion(TpNodo &lista, int pos){
	TpNodo temp=lista, q=CrearNodo();
	int x=1;
	bool flag = false;
	
	if(pos==1){	//si no hay nodos
		InsertarInicio(lista);
		return;
	}
	
	while(temp->sgte != NULL && x!= pos){
		temp=temp->sgte;
		x++;
		if(x==pos){	// encuentra posicion
			flag=true;
		}
	}
	
	if(flag){
		q->sgte =temp;
		temp->ant->sgte=q;
		q->ant=temp->ant;
		temp->ant=q;	
	}
	else{
		cout<<"[!] Posicion "<<pos<< "NO encontrada"<<endl;
		system("pause");
	}
}


// MENU
void menu(){
	system("cls");
	cout<<endl;
	
	cout<<"\tLISTAS DOBLEMENTE ENLAZADAS "<<endl<<endl;
	cout<<"1.- INSERTAR Nodo al Inicio "<<endl;
	cout<<"2.- INSERTAR Nodo al Final "<<endl;
	cout<<"3.- INSERTAR por Posicion "<<endl;
	cout<<"4.- MOSTRAR elementos de Ida y Vuelta "<<endl;
	cout<<"5.- ELIMINAR Primer Nodo "<<endl;
	cout<<"6.- ELIMINAR ultimo Nodo "<<endl;
	cout<<"7.- ELIMINAR por Posicion "<<endl;
	cout<<"8.- BUSCAR y Reemplazar valores "<<endl;
	cout<<"\n0.- Salir"<<endl;
	Color(BLACK, LCYAN);
	cout<<"\nOpcion > ";
	Color(BLACK, WHITE);
}


// ELIMINAR NODO INICIAL
 void EliminarInicio(TpNodo &lista){
 	TpNodo temp=lista;
 	if(lista->sgte ==NULL){	// si solo hay un nodo
		lista=NULL;
		delete(temp);
		return;
	}
 	
 	lista=lista->sgte;
 	lista->ant=NULL;
 	cout<<"\n[+] Nodo eliminado Nr. " <<temp->dato<<endl;
 	delete(temp);
 	getch();
 	
 }

// ELIMINAR NODO FINAL
 void EliminarFinal(TpNodo &lista){
 	TpNodo p=lista;
 	if(lista == NULL){
 		cout<<"[!] Lista vacia"<<endl;
 		system("pause > nul");
		 return;
	 }
	 if(lista->sgte ==NULL){
	 	lista=NULL;
		cout<<"\nNodo eliminado Nr "<<p->dato<<endl;
		delete(p);
 		system("pause > nul");
	 	return;
	 }
	 	 
	 while(p->sgte != NULL){
	  	p=p->sgte;
	 }
	p->ant->sgte = NULL;
	cout<<"\nNodo eliminado Nr. " <<p->dato<<endl<<endl;
 	delete(p);
 	system("pause");
	 	
}


// ELIMINAR POR POSICION
void EliminarPosicion(TpNodo &lista, int pos){
 	TpNodo p=lista;
 	int x=1;
 	bool flag=false;
 	// Si es la primera posicion
 	if(pos==1){
	 	EliminarInicio(lista);
	 	return;
	 }
	 
 	while(p->sgte != NULL && x != pos){
 		p=p->sgte;
 		x++;
 		if(x==pos)
 			flag=true;
 	 }
 	if(flag = true){
		// Si es el ultimo nodo 	
		if(p->sgte ==NULL){
	 		EliminarFinal(lista);
	 		return;
	 	}
 		p->ant->sgte = p->sgte;
		p->sgte->ant= p->ant;
 		cout<<"\nNodo eliminado Nr. " <<p->dato<<endl<<endl;
 		delete(p);
 		system("pause");
 	}
 	else{
 		cout<<"ERROR Posicion ingresada No Existe..."<<endl;
 		system("pause >nul");
	 }
 	
 }
 

// BUSCAR Y REEMPLAZAR 
void BuscaReemplaza(TpNodo lista, int b, int r){
  	TpNodo p=lista;
  	bool flag = false;
  	while(p!=NULL){
  		if(p->dato ==b){
  			p->dato=r;	
  			flag=true;
		  }
  			
  		p=p->sgte;	
	  }
  	if(flag==false){
  		cout<<"Valor "<<b<< " no encontrado en la lista"<<endl;
  		system("pause");
	  }
  	
  }


// MOSTRAR LISTA 
void MostrarLista(TpNodo lista){
 	TpNodo p=lista, t=NULL;
	int	n=1;
	
	Color(BLACK,YELLOW);
	cout<<"\nLISTA DE IDA"<<endl;
	while(p!=NULL){
		cout<<"Nodo ["<<n<<"] con valor > "<<p->dato<<endl;
		t=p;
		p=p->sgte;
		n++;
	}
	
	p=t;
	n=n-1;
	cout<<"\nLISTA DE VUELTA"<<endl;
	while(p!=NULL){
		cout<<"Nodo ["<<n<<"] con valor > "<<p->dato<<endl;
		p=p->ant;
		n--;
	}
	Color(BLACK,WHITE);
	
	system("pause > nul");
  }
  

// MAIN
int main(){
	TpNodo t=NULL, lista=NULL, p=NULL, q=NULL;
	int opc, n, pos, x, busca, reemp;
	do{
		menu();
		cin>>opc;
		switch(opc){
			case 1:{
				InsertarInicio(lista);
				break;
			}
			case 2:{
				InsertarFinal(lista);
				break;			
			}
			case 3:
				{
				if(lista ==NULL){
					cout<<"\n[!] Lista vacia"<<endl;
					getch();
				}
				else{
					cout<<"Ingresar posicion > ";cin>>pos;
					if(pos>0)
						InsertarPosicion(lista, pos);
					else{
						cout<<"\nERROR: Solo valores mayores que 0"<<endl;
						getch();
					}			
				}	

			break;
			}
		
			case 4:
			{
				MostrarLista(lista);
				
				break;
			}
			case 5:
				{
				EliminarInicio(lista);
				break;	
				}
			case 6:
				{
				EliminarFinal(lista);	
				break;
				}
			case 7:
			{
				if(lista==NULL){
					cout<<" Error: Lista Vacia..no permite esat opcion "<<endl;
					system("pause");
				}
				else{
					cout<<"Insertar Posicion---> ";cin>>pos;
					EliminarPosicion(lista, pos);
					
				}
				
				break;
			}	
			case 8:
			{
				if(lista==NULL){
					cout<<"[!] Lista vacia"<<endl;
					system("pause");
				}
				else{
					cout<<"Insertar el valor a Buscar-------> ";cin>>busca;
					cout<<"Insertar el valor a Reemplazar---> ";cin>>reemp;
					if(busca > 0 && reemp > 0)
						BuscaReemplaza(lista, busca, reemp);
					else{
						cout<<"ERROR: Solo permite valores > cero "<<endl;
						system("pause");
					}
				}
				
				break;
			}	
		}//switch
		
		
	
		
	}while(opc !=0);
	
	return 0;
}
