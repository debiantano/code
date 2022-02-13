#include <stdlib.h>
#include <math.h>
#include <GL/glut.h>
void init(void);
void display(void);
void reshape(int,int);
int main(int argc, char** argv)
{
glutInit(&argc, argv);
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);
glutInitWindowSize(500,500);
glutInitWindowPosition(100,100);
glutCreateWindow("test123");

init();

glutDisplayFunc(display);
glutReshapeFunc(reshape);
glutMainLoop();
return 0;
}

void init(void){
    glClearColor(0.0,0.0,0.0,0.0); //parametros: rojo, amarillo, azul, el cuarto es el parametro alpha
    glShadeModel(GL_FLAT);
}

void display(void){
    GLfloat ang, radio = 8.0f, x, y;
    glClear(GL_COLOR_BUFFER_BIT);

    glPushMatrix(); // salva el estado actual de la matriz

    glColor3f(1.0,1.0,1.0);
    glPointSize(5);

    glBegin(GL_POINTS);

    for (ang = 0.0f; ang < 2 * M_PI; ang += 2*M_PI/10){
        x = radio * sin(ang);
        y = radio * cos(ang);
        glVertex2f(x,y);
    }
    glEnd();
    glPopMatrix(); // reecupera el estado del matriz

    glFlush();
}

void reshape(int w, int h){
    glViewport(0,0,(GLsizei)w, (GLsizei)h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(-10.0,10.0,-10.0,10,-10.0,10.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}
