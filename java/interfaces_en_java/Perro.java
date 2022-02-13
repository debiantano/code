
package paquete1;

public class Perro implements Animal, SerVivo{

    @Override
    public void mostrar_tipo_animal() {
        System.out.println("Soy un mamifero");
    }

    @Override
    public String mostrar_nombre() {
        return "Mi nombre es Firulais";
    }
    
    @Override
    public void mostrar_vida(){
        System.out.println("Progaramando en java");
    }

}
