package temporales;

import java.util.Scanner;
import javax.swing.JOptionPane;

class Animal{}

class Mamifero extends Animal{}

class Reptil extends Animal{}

class Perro extends Mamifero{}

public class principal {

    public static void main(String[] args) {
        Animal animal = new Animal();
        Mamifero mamifero = new Mamifero();
        Perro perro = new Perro();
        
        System.out.println("El animal es instancia de perro? "+(animal instanceof Perro));
        System.out.println("El perro es instancia de animal? "+(perro instanceof Animal));
        
    }
}

