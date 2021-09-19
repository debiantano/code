
package abstracto;

public class Principal {
    public static void main(String[] args) {
        Planta planta = new Planta();
        planta.alimentarse();
        
        AnimalCarnivoro leon = new AnimalCarnivoro();
        leon.alimentarse();
    }
}
