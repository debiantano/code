/* Ingresar nombres de 10 alumnos (máximo 30 caracteres por nombre), por cada
uno de ellos ingresar 4 notas (deben estar entre 0 y 20), correspondientes a Parcial,
Final, trabajos e Intervención.
Se debe presentar el promedio por cada alumno (ajustar a enteros), mostrando sus
nombres. Finalmente obtener el promedio ponderado general. */

#include<iostream>
using namespace std;

int main(){
	string alumnos[10], nombre;
	int notas[10][4], filas[10], sumaFila=0;
	
	// Completando arreglo de nombres
	cout<<"NOMBRE DE LOS ALUMNOS"<<endl;
	for(int i=0;i<10;i++){
		cout<<"Alumno "<<i+1<<": ";
		cin>>nombre;
		fflush(stdin);
		if(nombre.length()<30){
			alumnos[i]=nombre;
		}
	}
	
	//completando notas de los alumnos
	cout<<"\tNOTAS DE LOS ALUMNOS"<<endl;
	for(int i=0;i<10;i++){
		for(int j=0;j<4;j++){
			cout<<"Nota ["<<i+1<<"]["<<j+1<<"]: ";
			cin>>notas[i][j];
		}
		cout<<endl;
	}
	
	
	//Algoritmo para el array de la suma de filas
	for(int i=0;i<10;i++){
		for(int j=0;j<4;j++){
			sumaFila+=notas[i][j];
		}
		filas[i]=sumaFila;
		sumaFila=0;
	}
	
	cout<<"   .:NOTAS ALUMNOS:."<<endl;
	cout<<"NOMBRES\t\tPROMEDIO"<<endl;
	for(int i=0;i<10;i++){
		cout<<alumnos[i]<<"\t->\t "<<filas[i]/4<<endl;
	}
	
	return 0;
}

