/* Dada una Matriz 4x5, ingresar valores enteros (positivos o negativos) y muestre en
un arreglo la suma de las filas y en otro arreglo, la suma de las columnas.
Adicionalmente obtener la suma total de las filas de este nuevo arreglo y el promedio
ponderado. */

#include<iostream>
using namespace std;

int main(){
	int matriz[4][5];
	int filas[4], columnas[5], sumaFila=0, sumaColumnas=0;
	
	cout<<"LLENANDO DATOS"<<endl;
	for(int i=0;i<4;i++){
		for(int j=0;j<5;j++){
			cout<<"Valor ["<<i<<"]["<<j<<"] >  ";
			cin>>matriz[i][j];
		}
	}
	
	cout<<"\nMOSTRANDO MATRIZ"<<endl;
	for(int i=0;i<4;i++){
		for(int j=0;j<5;j++){
			cout<<matriz[i][j]<<"  ";
		}
		cout<<endl;
	}
	
	cout<<endl;
	
	//Algoritmo para el array de la suma de filas
	for(int i=0;i<4;i++){
		for(int j=0;j<5;j++){
			sumaFila+=matriz[i][j];
		}
		filas[i]=sumaFila;
		sumaFila=0;
	}
	
	cout<<"ARRAY DE LA SUMA DE FILAS"<<endl;
	for(int i=0;i<4;i++){
		cout<<filas[i]<<" ";
	}
	
	//Algoritmo para el array de la suma de columnas
	for(int i=0;i<5;i++){
		for(int j=0;j<4;j++){
			sumaColumnas+=matriz[j][i];
		}
		columnas[i]=sumaColumnas;
		sumaColumnas=0;
	}
	
	cout<<"\n\nARRAY DE LA SUMA DE COLUMNAS"<<endl;
	for(int i=0;i<5;i++){
		cout<<columnas[i]<<" ";
	}
	
	return 0;
}
