#include<iostream>

using namespace std;

int main(){
	int pass;

	cout<<"Enter my password: ";
	cin>>pass;

	if(pass==123){
		cout<<"[+] Login success"<<endl;
	}else{
		cout<<"[-] Error login"<<endl;
	}

	return 0;
}
