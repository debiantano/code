package temporales;

import java.util.Scanner;
import javax.swing.JOptionPane;


public class Temporales {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        float numero;
        System.out.print("Digite un numero: ");
        numero=entrada.nextFloat();
        
        System.out.println("El numero es: "+numero);
    }  
}
