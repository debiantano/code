#include<stdio.h>
#include<iostream>
#include<string.h>
#include<stdlib.h>

using namespace std;

int main()
{
    char s[100] = "4.0840";
    
    cout<<"valor flotante: "<<strtod(s,NULL)<<endl;
    //printf("Float value : %4.3f\n",strtod(s,NULL));
    return 0;
}
