// Rellenando elementos de una matriz
#include<iostream>

using namespace std;

int main(){
	int matriz[2][2];
	
	for(int i=0;i<2;i++){
		for(int j=0;j<2;j++){
			cout<<"Valor ["<<i<<"]["<<j<<"]: ";
			cin>>matriz[i][j];
		}
	}
	
	cout<<"\Imprimiendo matriz\n"<<endl;
	for(int i=0;i<2;i++){
		for(int j=0;j<2;j++){
			cout<<matriz[i][j]<<"  ";
		}
		cout<<endl;
	}
	
	return 0;
}
