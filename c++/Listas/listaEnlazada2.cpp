// Ingresar n elementos en una lista enlazada y luego reportarlos.
// Los elementos que se ingresan se insertan al final de la lista.

#include <iostream>
using namespace std;

struct Nodo{
	int info;
	Nodo *sgte;
};

typedef Nodo *Lista;

void insertaAlFinal(Lista &L,int x);
void ingresoDeDatos(Lista &L);
void reporteDeDatos(Lista L);

int main(int argc, char *argv[]) {
	Lista L=NULL;
	ingresoDeDatos(L);
	reporteDeDatos(L);
	return 0;
}

void insertaAlFinal(Lista &L, int x)
{
	Lista nuevo,p;
	nuevo= new Nodo;
	nuevo->info=x;
	nuevo->sgte=NULL;
	if(L==NULL)
		L=nuevo;
	else	
	{
		p=L;
		while(p->sgte!=NULL){
			p=p->sgte;
		}
		p->sgte=nuevo;
	}
}

void ingresoDeDatos(Lista &L)
{
	int i,x,n;
	cout<<"Numero de elementos : ";
	cin>>n;
	for(i=1;i<=n;i++)
	{
		cout<<"Elemento "<<i<< ": ";
		cin>>x;
		insertaAlFinal(L,x);
	}
}

void reporteDeDatos(Lista L)
{
	Lista p;
	p=L;
	cout<<"Datos de la lista "<<endl;
	while(p!=NULL)
	{
		cout<<p->info<<endl;
		p=p->sgte;
	}
	cout<<endl;
}
