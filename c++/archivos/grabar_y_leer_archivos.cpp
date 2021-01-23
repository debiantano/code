/* Grabar datos en un archivo
out : limpia y graba
app : adiciona sobre lo existente

*/

#include<iostream>
#include<fstream>

using namespace std;
string nombre, direccion, dni;

int main(){
	// Crear un driver de salida
	ofstream Grabacion;
	// Abrir archivo
	Grabacion.open("c:\\Users\\advance\\Desktop\\temporal.txt",ios::out);
	// Operar con el archivo
	Grabacion<<"Nemesis"<<endl;
	Grabacion<<"Lucan 17-84 Venecia"<<endl;
	Grabacion<<"998-3465-661"<<endl;
	// Cerrar el archivo
	Grabacion.close();
	
	// LEER DATOS
	// Crear el archivo de lectura INPUT
	ifstream Lectura;
	//Ubicar y abrir archivo
	Lectura.open("c:\\Users\\advance\\desktop\\temporal.txt",ios::in);
	// Operar, leer los registros del archivo
	
	getline(Lectura,nombre);
		while(!Lectura.eof()){
		getline(Lectura,direccion);
		getline(Lectura,dni);
		
		cout<<"Nombre.................."<<nombre<<endl;
		cout<<"Direccion..............."<<direccion<<endl;
		cout<<"DNI....................."<<dni<<endl;
		getline(Lectura,nombre);
	}
	cout<<endl;
	system("pause");
	// Paso 5: Cerrar archivo
	Lectura.close();
		 
	return 0;
}
