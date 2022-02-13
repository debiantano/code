#include<iostream>

using namespace std;
void fComprobacion(int);

int main(){
	int pass;

	cout<<"Enter my password: ";
	cin>>pass;

	fComprobacion(pass);

	return 0;
}

void fComprobacion(int pass){

	if(pass==123){
		cout<<"[+] Login success"<<endl;
	}else{
		cout<<"[-] Error login"<<endl;
	}
}
