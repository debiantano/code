#include<stdio.h>
#include <string.h> 

void hacer_algo(char *Buffer) 
{ 
 char MyVar[128]; 
 strcpy(MyVar,Buffer);
 printf(MyVar);
} 
int main (int argc, char **argv) 
{ 
 hacer_algo(argv[1]); 
} 
