#include <GL/glut.h>

int main (int argc, char **argv){
    glutInitWindowSize (640, 480);                      // Fijar tamaño y posición inicial de las ventanas
    glutInitWindowPosition (0, 0);
    glutInitDisplayMode (GLUT_RGBA | GLUT_DOUBLE);      // Seleccionar modo de display: RGBA y doble buffer
    glutInit (&argc, argv);                             // Inicializar la librería GLUT
    // Código del programa
    // ...
}
