
package paquete1;

public class Principal {
    public static void main(String[] args) {
        Perro perro = new Perro();
        
        perro.mostrar_tipo_animal();
        System.out.println(perro.mostrar_nombre());
        
        perro.mostrar_vida();
    }
}
