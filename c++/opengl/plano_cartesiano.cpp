#include <stdlib.h>
#include <math.h>
#include <GL/glut.h>

void ejes(void){
    glBegin(GL_LINES);
    glVertex2f(-10.0,0.0);
    glVertex2f(10.0,0.0);
    glVertex2f(0,-10);
    glVertex2f(0,10);
    glEnd();
}

void reshape(int w, int h){
    //glViewport(0,0,(GLsizei)w, (GLsizei)h);
    //glMatrixMode(GL_PROJECTION);
    //glLoadIdentity();
    glOrtho(-10.0,10.0,-10.0,10,-10.0,10.0);
    //glMatrixMode(GL_MODELVIEW);
    //glLoadIdentity();
}


void display(void){
    glClear(GL_COLOR_BUFFER_BIT);
    glPushMatrix(); // salva el estado actual de la matriz

    glColor3f(1.0,0.0,0.0);
    ejes();

    glPopMatrix();
    glFlush();
}


int main(int argc, char** argv){
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);
    glutInitWindowSize(500,500);
    glutInitWindowPosition(100,100);
    glutCreateWindow(argv[0]);

    glClearColor(1.0,1.0,1.0,0.0); //parametros: rojo, amarillo, azul, el cuarto es el parametro alpha
    //glShadeModel(GL_SMOOTH);

    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutMainLoop();
    return 0;
}
