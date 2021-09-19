#include<iostream>

using namespace std;
void fComprobacion(string);

int main(){
	string pass;

	cout<<"Enter my password: ";
	cin>>pass;

	fComprobacion(pass);

	return 0;
}

void fComprobacion(string pass){
	if(pass == "passwd"){
		cout<<"[+] Login success"<<endl;
	}else{
		cout<<"[-] Error login"<<endl;
	}
}
