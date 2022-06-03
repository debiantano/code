// Ingresar n elementos reales en una lista y calcular el mayor, el menor y el promedio

#include <iostream>
using namespace std;

struct Nodo{
	float info;
	Nodo *sgte;
};

typedef Nodo *Lista;

void insertaAlFinal(Lista &L,float x);
void ingresoDeDatos(Lista &L);
void reporteDeDatos(Lista L);
float mayor(Lista L);
float menor(Lista L);
float promedio(Lista L);

int main(int argc, char *argv[]) {
	Lista L=NULL;
	ingresoDeDatos(L);
	reporteDeDatos(L);
	cout<<"El mayor es : "<<mayor(L)<<endl;
	cout<<"El menor es : "<<menor(L)<<endl;
	cout<<"El prmedio es : "<<promedio(L)<<endl;
	return 0;
}

void insertaAlFinal(Lista &L, float x)
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
		while(p->sgte!=NULL)
			p=p->sgte;
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

float mayor(Lista L)
{
	float may;
	Lista p;
	may=L->info;
	p=L;
	while(p!=NULL)
	{
		if(p->info>may)
			may=p->info;
		p=p->sgte;
	}
	return may;
}

float menor(Lista L)
{
	float men;
	Lista p;
	men=L->info;
	p=L;
	while(p!=NULL)
	{
		if(p->info<men)
			men=p->info;
		p=p->sgte;
	}
	return men;
}

float promedio(Lista L)
{
	float s=0;
	int c=0;
	Lista p;
	
	p=L;
	while(p!=NULL)
	{
		s=s + p->info;
		c++;
		p=p->sgte;
	}
	return s/c;
}
