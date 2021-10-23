#include <stdlib.h>
#include <math.h>
#include <GL/glut.h>
void ejes(void);
void circunferencia1(int,int,float);
void circunferencia2(int,int,float);
void circunferencia3(int,int,float);


void init(void);
void display(void);
void reshape(int,int);

int main(int argc, char** argv){
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);
    glutInitWindowSize(500,500);
    glutInitWindowPosition(100,100);
    glutCreateWindow(argv[0]);

    init();
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutMainLoop();
    return 0;
}


void ejes(void){
    glBegin(GL_LINES);
    glVertex2f(-9.0,0.0);
    glVertex2f(9.0,0.0);
    glVertex2f(0,-9);
    glVertex2f(0,9);
    glEnd();
}


void circunferencia1(int h,int k,float radio){
    GLfloat ang, x, y;
    glBegin(GL_POINTS);
    for (ang = 0.0f; ang < 2 * M_PI; ang += 2*M_PI/10)
        {
            x = h+radio * cos(ang);
            y = k+radio * sin(ang);
            glVertex2f(x,y);
        }
    glEnd();
}


//void circunferencia2(int h,glColor3f(0.0,0.0,1.0);int k,float radio)
void circunferencia2(int h, int k,float radio){
    GLfloat ang, x, y;
    glBegin(GL_LINE_LOOP);
    for (ang = 0.0f; ang < 2 * M_PI; ang += 2*M_PI/10)
        {
            x = h+radio * cos(ang);
            y = k+radio * sin(ang);
            glVertex2f(x,y);
        }
    glEnd();
}


void circunferencia3(int h,int k,float radio){
    GLfloat ang, x, y;
    glBegin(GL_POLYGON);
    for (ang = 0.0f; ang < 2 * M_PI; ang += 2*M_PI/10)
        {
            x = h+radio * cos(ang);
            y = k+radio * sin(ang);
            glVertex2f(x,y);
        }
    glEnd();
}


void init(void)
{
glClearColor(1.0,1.0,1.0,0.0); //parametros: rojo, amarillo, azul, el cuarto es el parametro alpha
glShadeModel(GL_FLAT);
}


void display(void){
    glClear(GL_COLOR_BUFFER_BIT);
    glPushMatrix(); // salva el estado actual de la matriz




    glColor3f(0.0,0.0,1.0);
    ejes();


    glColor3f(1.0,0.0,0.0);
    glPointSize(4);
    circunferencia1(-5,5,2);
    glColor3f(0.0,1.0,0.0);
    circunferencia2(0,5,2);
    glLineWidth(4.0);
    glColor3f(0.0,0.0,1.0);
    circunferencia2(5,5,2);


    glColor3f(0.0,0.0,1.0);
    circunferencia3(-5,-5,2);


    glColor3f(0.0,0.0,1.0);
    glLineWidth(2.0);
    glLineStipple(1,0xAAAA);
    glEnable(GL_LINE_STIPPLE);
    circunferencia2(0,-5,2);
    glDisable(GL_LINE_STIPPLE);


    glColor3f(0.0,1.0,.0);
    circunferencia3(5,-5,2);


    glLineWidth(2.0);
    glColor3f(0.0,0.0,1.0);
    glLineStipple(1,0xAAAA);
    glEnable(GL_LINE_STIPPLE);
    circunferencia2(5,-5,2);
    glDisable(GL_LINE_STIPPLE);


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
