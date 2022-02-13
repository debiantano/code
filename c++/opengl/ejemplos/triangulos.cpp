#include <GL/glut.h>
#include <windows.h>
#include<stdlib.h>
#include<math.h>
#include <stdlib.h>

double cuadrado_x=0.0;
double cuadrado_y=0.0;
double gira=0.0;




void mostrar (void);
void inicializacion (void);
void Figuras();


int main (int argc, char *argv[]) {

    glutInit (&argc, argv);
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB );
    glutInitWindowPosition(100,100);
    glutInitWindowSize (500, 500);
    glutCreateWindow ("U2Practica2");

    inicializacion();
    glutDisplayFunc (mostrar);
    glutMainLoop();
    return 0;
}

void mostrar (void) {
    glClear (GL_COLOR_BUFFER_BIT );

    Figuras();

}


void Figuras(){
    //GL_TRIANGLE_FAN
    glClear(GL_COLOR_BUFFER_BIT);
         glColor3f(1.0,1.0,0.0);
         glBegin(GL_TRIANGLE_FAN);
        glVertex3f(0, 30,0.0);
        glVertex3f(-30, 10,0.0);
        glVertex3f(-20,-30,0.0);
        glVertex3f(20,-30,0.0);
        glVertex3f(30,10,0.0);
     glEnd();
     glFlush();

     //GL_TRIANGLE_STIRP
     glColor3f(1.0,0.0,1.0);
     glBegin(GL_TRIANGLE_STRIP);
        glVertex3f(40, 0,0.0);
        glVertex3f(60, 30,0.0);
        glVertex3f(120, 30,0.0);
        glVertex3f(140, 0,0.0);
        glVertex3f(40, 0,0.0);
    glEnd();
    glFlush();

    //GL_TRIANGLES
    glColor3f(0.0,0.0,1.0);
     glBegin(GL_TRIANGLES);
        glVertex2f(60, 80);
        glVertex2f(80, 50);
        glVertex2f(90, 90);
    glEnd();
    glFlush();
    glColor3f(1.0,0.0,1.0);
    glBegin(GL_TRIANGLES);
        glVertex2f(60, 80);
        glVertex2f(90, 90);
        glVertex2f(60, 110);
    glEnd();
    glFlush();
    glColor3f(0.0,0.0,1.0);
    glBegin(GL_TRIANGLES);
        glVertex2f(60, 80);
        glVertex2f(60, 110);
        glVertex2f(30, 90);
    glEnd();
    glFlush();
    glColor3f(1.0,0.0,0.0);
    glBegin(GL_TRIANGLES);
        glVertex2f(60, 80);
        glVertex2f(30, 90);
        glVertex2f(40, 50);
    glEnd();
    glFlush();
    glColor3f(0.0,1.0,1.0);
    glBegin(GL_TRIANGLES);
        glVertex2f(60, 80);
        glVertex2f(40, 50);
        glVertex2f(80, 50);
    glEnd();
    glFlush();

    //GL_TRIANGLE2
    glColor3f(1.0,0.0,1.0);
    glBegin(GL_TRIANGLES);
        glVertex2f(-140, 0);
        glVertex2f(-125, 30);
        glVertex2f(-110, 0);
    glEnd();
    glFlush();
    glColor3f(0.0,1.0,1.0);
    glBegin(GL_TRIANGLES);
        glVertex2f(-125, 30);
        glVertex2f(-95, 30);
        glVertex2f(-110, 00);
    glEnd();
    glFlush();
    glColor3f(1.0,0.0,0.0);
    glBegin(GL_TRIANGLES);
        glVertex2f(-110, 00);
        glVertex2f(-95, 30);
        glVertex2f(-80, 0);
    glEnd();
    glFlush();
    glColor3f(1.0,0.0,1.0);
    glBegin(GL_TRIANGLES);
        glVertex2f(-80, 0);
        glVertex2f(-95, 30);
        glVertex2f(-65, 30);
    glEnd();
    glFlush();
    glColor3f(0.0,1.0,1.0);
    glBegin(GL_TRIANGLES);
        glVertex2f(-80, 0);
        glVertex2f(-65, 30);
        glVertex2f(-50, 0);
    glEnd();
    glFlush();

}

void inicializacion (void) {
    glClearColor(0.0, 0.0, 0.0, 0.0);
    glMatrixMode(GL_PROJECTION);
    gluOrtho2D(-250,250,-250,250);
}
