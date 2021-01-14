/* Realize un programa que lea una matriz de 3x3 y cree su matriz transpuesta. La matriz transpuesta es aquella en la que la colummna 
'i' era la fila 'i' de la matriz original

	|1 2 3|		|1 4 7|
	|4 5 6|	--> |2 5 8|
	|7 8 9|		|3 6 9|
*/

#include<iostream>
using namespace std;

int main(){
	int numeros[3][5];
	
	for(int i=0;i<3;i++){
		for(int j=0;j<5;j++){
			cout<<"Digite un numero["<<i<<"]["<<j<<"]: ";
			cin>>numeros[i][j];
		}
	}
	cout<<"\nMATRIZ ORIGINAL"<<endl;
	for(int i=0;i<3;i++){
		for(int j=0;j<5;j++){
			cout<<numeros[i][j]<<"  ";
		}
		cout<<endl;
	}

	cout<<"MATRIZ TRANSPUESTA"<<endl;
	for(int i=0;i<5;i++){
		for(int j=0;j<3;j++){
			cout<<numeros[j][i]<<"  ";
		}
		cout<<endl;
	}
	
	
	return 0;
}
