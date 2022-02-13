#include<GL/glut.h>
//#include<windows.h>

void inicio(){
	glClearColor(0.0, 0.0, 0.0, 0.0);
	glMatrixMode(GL_PROJECTION);
	gluOrtho2D(-10, 10, -10, 10);
}

void pantalla(){
	glClear(GL_COLOR_BUFFER_BIT);

	glColor3f(0.5,0.5,0.0);
	glBegin(GL_QUADS);
		glVertex2i(5,5);
		glVertex2i(-5,5);
		glVertex2i(-5,-5);
		glVertex2i(5,-5);
	glEnd();

	glColor3f(1.0,0.5,0.0);
	glBegin(GL_QUADS);
		glVertex2f(2.5,2.5);
		glVertex2f(-2.5,2.5);
		glVertex2f(-2.5,-2.5);
		glVertex2f(2.5,-2.5);
	glEnd();

	glFlush();
}


int main(int argc, char **argv){
	glutInit(&argc,argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowPosition(50,50);
	glutInitWindowSize(500,500);
	glutCreateWindow("HELLO");

	inicio();
	glutDisplayFunc(pantalla);
	glutMainLoop();

	return EXIT_SUCCESS;
}
