
#include<iostream>
#include<fstream>

using namespace std;

void lectura(){
	ifstream archivo;
	string texto;
	
	archivo.open("temporal.txt",ios::in); // abrimos el archivo en modo lectura
	
	if(archivo.fail()){
		cout<<"No se pudo abrir el archivo"<<endl;
		exit(1);
	}
	
	while(!archivo.eof()){ // mientras no sea el final del archivo
		getline(archivo,texto);
		cout<<texto<<endl;		
	}
}

int main(){
	lectura();
	
	return 0;
}
