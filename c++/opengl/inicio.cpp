#include <GL/glut.h>

int main (int argc, char **argv){
    // Fijar tamaño y posición inicial de las ventanas
    glutInitWindowSize (640, 480);
    glutInitWindowPosition (0, 0);
    // Seleccionar modo de display: RGBA y doble buffer
    glutInitDisplayMode (GLUT_RGBA | GLUT_DOUBLE);
    // Inicializar la librería GLUT
    glutInit (&argc, argv);
    // Código del programa
    // ...
}
