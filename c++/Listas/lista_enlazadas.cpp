// Ingresar n elementos en una lista enlazada y luego reportarlos.
// Los elementos que se ingresan se insertan al inicio de la lista.

#include <iostream>

using namespace std;

struct Nodo{
	int info;
	Nodo *sgte;
};

typedef Nodo *Lista;

void insertaAlInicio(Lista &L,int x);
void ingresoDeDatos(Lista &L);
void reporteDeDatos(Lista L);

int main(int argc, char *argv[]) {
	Lista L=NULL;
	ingresoDeDatos(L);
	reporteDeDatos(L);
	return 0;
}

void insertaAlInicio(Lista &L,int x)
{
	Lista nuevo;
	nuevo = new Nodo;
	nuevo->info = x;
	nuevo->sgte=L;
	L=nuevo;
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
		insertaAlInicio(L,x);
	}
}

void reporteDeDatos(Lista L)
{
	Lista p;
	p=L;
	cout<<"\nDatos de la lista "<<endl;
	while(p!=NULL)
	{
		cout<<p->info<<endl;
		p=p->sgte;
	}
	cout<<endl;
}
