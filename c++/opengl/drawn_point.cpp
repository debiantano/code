#include<iostream>
#include<GL/glut.h>

void dibujar(){
    glClear(GL_COLOR_BUFFER_BIT);    //limpieza se basa en el color q esta en el buffer

    glBegin(GL_POINTS); //Inicializar punto
    glVertex2d(100,100);  // ubicacion del punto (posicion)
    glVertex2d(200,200);
    glVertex2d(300,300);
    glVertex2d(400,400);
    glEnd();

    glFlush();  // muestra y vacea el buffer
}

void iniciar(){
    glClearColor(0,1,0,1);  // color a usar para limpiar la pantalla
    glPointSize(10); // Tamaño del punto
    glColor3f(1.f,0,0);   // color flotante
    glOrtho(800,0,600,0,-1,1);  // camara
}

int main(int argc, char *args[]){
    glutInit(&argc,args);
    glutInitDisplayMode(GLUT_RGB|GLUT_SINGLE); //un solo buffer a usar
    glutInitWindowPosition(60,60);  // posicion de la ventana
    glutInitWindowSize(800,600); //tamaño  de la ventana
    glutCreateWindow("test 123");   // nombre del programa

    glutDisplayFunc(dibujar);  //que funcion usar

    iniciar();

    glutMainLoop(); // lo que se va a repetir hasta acá

    return 0;
}
