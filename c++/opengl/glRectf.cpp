#include <iostream>
#include<GL/glut.h> // Incluye automáticamente <GL / gl.h> y <GL / glu.h> 

void myDisplay1(void)
{
	glClearColor(0.0, 0.0, 0.0, 0.0);
	glClear(GL_COLOR_BUFFER_BIT);

	glColor3f(0.5f, 0.5f, 0.0f);
	glRectf(-0.0f, -0.0f, 0.2f, 0.5f);
	glFlush();
}
int main(int argc, char* argv[]) // Función principal con parámetros de línea de comando
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);
	glutInitWindowPosition(100, 100);
	glutInitWindowSize(400, 400);
	glutCreateWindow("Hello World");

	glutDisplayFunc(myDisplay1);
	glutMainLoop();
	return 0;
}
