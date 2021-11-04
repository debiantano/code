#include <iostream>
#include <math.h>
#include <GL/glut.h>
#include <stdio.h>
#include <stdlib.h>

void init(void);
void display(void);
void reshape(int, int);
void circunferencia_punto_medio(int,int,int);


int px0=-30,py0=0,px1=48,py1=28;
using namespace std;

int main(int argc, char** argv){
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);
    glutInitWindowSize(600, 600);
    glutInitWindowPosition(100,100);
    glutCreateWindow("Algoritmo Basico");

    init();
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutMainLoop();
    return 0;
}

void init(void){
    glClearColor(1.0,1.0,1.0,0.0); //parametros: rojo, amarillo y azul, el cuarto es el parametro alpha
    glShadeModel(GL_SMOOTH);
}

void display(void){
    glClear(GL_COLOR_BUFFER_BIT);
    glPushMatrix(); // salva el estado actual de la matriz
    glColor3f(0,0,1); // Azul
    glPointSize(3); // Fije el grosor de pixel = 2
    glColor3f(1,0,0);
    circunferencia_punto_medio(0,0,30);
    circunferencia_punto_medio(0,0,1);
    circunferencia_punto_medio(-20,-20,10);

    glPopMatrix(); // recupera el estado del matriz
    glFlush();
}

void reshape(int w, int h){
    glViewport(0,0,(GLsizei)w, (GLsizei)h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(-50.0, 50.0, -50.0, 50.0, -1.0, 1.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}

void circunferencia_punto_medio(int h,int k,int R){
    // discretizacion valida en el II octante
    int x=0;
    int y=R,d=1-R;
    glBegin(GL_POINTS);
        glVertex2f(x,y);
        while (x<y){
            if (d<0)
                d+=2*x+3;
            else{
                d+=2*(x-y)+5;
                y--;
                }
            x++;
            glVertex2f(x+h,y+k);
            glVertex2f(-x+h,y+k);
            glVertex2f(-y+h,x+k);
            glVertex2f(-y+h,-x+k);
            glVertex2f(-x+h,-y+k);
            glVertex2f(x+h,-y+k);
            glVertex2f(y+h,-x+k);
            glVertex2f(y+h,x+k);
        }
    glEnd();
}
