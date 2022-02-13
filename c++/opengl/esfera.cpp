#include<stdlib.h>
#include<GL/glut.h>

void init (){
	glClearColor(0.0, 0.0, 0.0, 0.0);
	glShadeModel(GL_FLAT);
}

void display(void){
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(9.0,9.0,9.0);
	glutWireSphere(2.0,30,36);
	glutSwapBuffers();
}

void reshape(int w, int h){
	glMatrixMode(GL_PROJECTION);
	gluPerspective(50.0,w/(GLfloat)h, 3.0, 90.0);
	glMatrixMode(GL_MODELVIEW);
	gluLookAt(2.0, 4.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
}

int main(int argc, char** argv){
    glutInit(&argc,argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowPosition(10,10);
    glutInitWindowSize(800,600);
    glutCreateWindow("HELLO");

    init();
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutMainLoop();

    return 0;
}
