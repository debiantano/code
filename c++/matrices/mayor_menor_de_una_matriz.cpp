// calculo del elemento mayor y menor de una matriz
#include<iostream>
using namespace std;

int main(){
	int matriz[2][3],i,j,mayor,menor;
	
	cout<<"Llenando matriz"<<endl;
	for(i=0;i<2;i++){
		for(j=0;j<3;j++){
			cout<<"> ";
			cin>>matriz[i][j];	
		}
	}
	
	cout<<"\nImpresion de matriz"<<endl;
	for(i=0;i<2;i++){
		for(j=0;j<3;j++){
			cout<<matriz[i][j]<<" ";	
		}
		cout<<endl;
	}
	
	mayor=matriz[0][0];
	menor=matriz[0][0];
	for(i=0;i<2;i++){
		for(j=0;j<3;j++){
			if(mayor<matriz[i][j]){
				mayor=matriz[i][j];
			}
			if(menor>matriz[i][j]){
				menor=matriz[i][j];
			}
		}
	}
	
	cout<<"\nEl mayor numero es: "<<mayor<<endl;
	cout<<"\nEl menor numero es: "<<menor<<endl;
	
	return 0;
}
