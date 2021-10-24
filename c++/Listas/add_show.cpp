#include<iostream>

using namespace std;

struct nodo{
	int valor;
	nodo *siguiente;
}*pi, *pa, *pf;

void insertar(int valor){
	if(pi==NULL){
		pi=new (nodo);
		pi->valor=valor;
		pf=pi;
	}else{
		pa=new (nodo);
		pf->siguiente=pa;
		pa->valor=valor;
		pf=pa;
	}
	pf->siguiente=NULL;
}


void mostrarElemento(){
	pa=pi;
	int i=1;
	while(pa!=NULL){
		cout<<"Elemento ["<<i<<"]: "<<pa->valor<<endl;
		i++;
		pa=pa->siguiente;
	}
}

int main(){
	int valor;
	char rpta;
	
	do{
		cout<<"Ingrese valor: ";cin>>valor;
		insertar(valor);
		cout<<"Desea seguir ingresando eleemnto (s/n): ";cin>>rpta;
	}while(rpta=='s');
	mostrarElemento();
	
	return 0;
}
