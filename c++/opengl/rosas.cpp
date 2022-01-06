#include <cmath>
#include <iostream>
#include <GL/glut.h>
using namespace std;
GLint n; //2n is number of petals on the rose
void init(){
	glClearColor (1.0, 1.0, 1.0, 1.0);			//set the background color to white
	glColor3f (0.0, 0.0, 0.0); 					//set the foreground color to black
	glMatrixMode (GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(-3.0, 3.0, -3.0, 3.0);
	glMatrixMode (GL_MODELVIEW);
}

// The purpose of drawSierpinski() is to display the mathematical
// function y = exp(-x) cos (2 PI x) in the window.
void drawCurve(){
	const double PI = 3.14159;      //PI in radians
	GLdouble radians;               //theta in radians
	//Clear the background
	glClear (GL_COLOR_BUFFER_BIT);
	//set the foreground color
	glColor3ub (200, 55, 134);
	//(x, y) is a point on the parametric curve
	GLdouble x, y;
	//plot points from the parametric curve
	glBegin (GL_POLYGON);
		glVertex2d(0.0, 0.0);
		for (GLdouble theta = 0; theta <= 360.0; theta += 2.0){
			radians = theta * PI/180.0;            //convert PI to radians
			x = 2.0 * cos(n * radians) * cos(radians);
			y = 2.0 * cos(n * radians) * sin(radians);
			//cout << x << " " << y << endl;
			glVertex2d (x, y);
		}
	glEnd();
	//send all output to the display
	glFlush();
}

int main(int argc, char** argv){
	//initialize the OpenGL Utility Toolkit
	glutInit(&argc, argv);
	//set the display mode--a single display buffer and colors
	//specified using amounts of red, green, & blue
	glutInitDisplayMode( GLUT_SINGLE | GLUT_RGB);
	//request a screen window 500 pixels wide by 500 pixels high
	glutInitWindowSize(500, 500);
	//specify the window position
	glutInitWindowPosition(0,0);
	//Get the number of petals to use
	cout << "Input an integer n which represents the number of petals/2\n";
	cin >> n;
	glutCreateWindow("Parametric Curve");
	glutDisplayFunc(drawCurve);
	init();
	glutMainLoop();
	return 0;
}
