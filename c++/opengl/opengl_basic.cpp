// No Funcional
#include<windows.h>
#include<GL/glu.h>

void inicio(){
    glMatrixMode(GL_PROJECTION); // hacer el uso de la pantalla
    gluOrtho2D(-50,50,-50,50); // indicar las dimnsiones q queramos (plano cartesiano)
    glClearColor(0.0,0.0,1.0,0.0); // color de fondo mediante punto flotante
}

void pantalla(){
    glClear(GL_COLOR_BUFFER_BIT);

    // codigo del programa

    glFlush();
}


main(int argc, char *argv[]){
    glutInit(&argc, argv);
    glutInitWindowSize(500,500); // tamaño de la pantalla
    glutInitWindowPosition(200,200); // en q pate de la pantalla aparezca la ventana
    glutInitDisplayMode(GLUT_RGB|GLUT_SINGLE); // de q forma manejar los colores

    glutCreateWindow("Test123"); // titulo del programa
    inicio();
    glutDisplayFunc(pantalla);


    glutMainLoop(); // para q el programa se repita y no se cierre
    return EXIT_SUCCESS;

}
