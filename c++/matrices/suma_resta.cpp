
#include<iostream>
#include<time.h>
#include<stdlib.h>
#define N 3

using namespace std;

int main(){
	int matriz1[N][N], matriz2[N][N], suma[N][N], resta[N][N];	
	srand(time(NULL));
    
 	cout<<"MATRIZ 1"<<endl;
   	for(int i=0;i<N;i++){
   		for(int j=0;j<N;j++){
   			matriz1[i][j]=rand()%(100);
   			cout<<matriz1[i][j]<<" ";
		   }
		   cout<<endl;
	   }
	
	cout<<"\nMATRIZ 2"<<endl;
	for(int i=0;i<N;i++){
   		for(int j=0;j<N;j++){
   			matriz2[i][j]=rand()%(100);
   			cout<<matriz2[i][j]<<" ";
		   }
		   cout<<endl;
	   }

	cout<<"\n--------------------------\n";
	cout<<"\nMATRIZ SUMA"<<endl;
	for(int i=0;i<N;i++){
   		for(int j=0;j<N;j++){
   			suma[i][j]=matriz1[i][j]+matriz2[i][j];
   			cout<<suma[i][j]<<" ";
		   }
		   cout<<endl;
	   }
	   
	cout<<"\nMATRIZ RESTA"<<endl;
	for(int i=0;i<N;i++){
   		for(int j=0;j<N;j++){
   			resta[i][j]=matriz1[i][j]-matriz2[i][j];
   			cout<<resta[i][j]<<" ";
		   }
		   cout<<endl;
	   }
	
	return 0;
}
