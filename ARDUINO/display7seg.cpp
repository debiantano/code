int pausa=1000;

void setup(){
  pinMode(7,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(12,OUTPUT);
  pinMode(13,OUTPUT);
  }

void display(int a, int b, int c, int d, int e, int f, int g){
  digitalWrite(7,a);
  digitalWrite(8,b);
  digitalWrite(9,c);
  digitalWrite(10,d);
  digitalWrite(11,e);
  digitalWrite(12,f);
  digitalWrite(13,g);
  }

void loop(){
  display(1,1,1,1,1,1,0); //0
  delay(pausa);
  display(0,1,1,0,0,0,0); //1
  delay(pausa);
  display(1,1,0,1,1,0,1); //2
  delay(pausa);
  display(1,1,1,1,0,0,1); //3
  delay(pausa);
  display(0,1,1,0,0,1,1); //4
  delay(pausa);
  display(1,0,1,1,0,1,1); //5
  delay(pausa);
  display(1,0,1,1,1,1,1); //6
  delay(pausa);
  display(1,1,1,0,0,0,0); //7
  delay(pausa);
  display(1,1,1,1,1,1,1); //8
  delay(pausa);
  display(1,1,1,0,0,1,1); //9
  delay(pausa);
  }

  
