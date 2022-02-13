#include <stdlib.h>
#include <time.h>
#include<iostream>
using namespace std;
 
int main()
{
    int num, c;
    srand(time(NULL));
    
    cout<<"NUMERO ALEATORIO ENTRE 1 y 10"<<endl;
    num =1+rand()%(10);
    cout<<"El numeros es: "<<num<<endl;
    
    return 0;
}
