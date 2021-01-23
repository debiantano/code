#include<iostream>
using namespace std;

void valor(int &num1, int &num2){
    cout<<"El valor del primer numero es: "<<num1<<endl;
    cout<<"El valor del segundo numero es: "<<num2<<endl;

    num1=88;
    num2=11;
}

int main(){
    int num1, num2;
    cout<<"Digite un numero: ";
    cin>>num1;
    cout<<"Digite otro numero: ";
    cin>>num2;
    cout<<endl;
    valor(num1,num2);

    cout<<"El nuevo valor del primer numero es: "<<num1<<endl;
    cout<<"El nuevo valor del segundo numero es: "<<num2<<endl;

    return 0;
}
