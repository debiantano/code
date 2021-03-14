package temporales;

import java.util.Scanner;
import javax.swing.JOptionPane;


public class principal {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        String nombre1;
        String nombre2;
        
        System.out.print("Digite el primer nombre: ");
        nombre1=entrada.nextLine();
        
        System.out.print("Digite el segundo nombre: ");
        nombre2=entrada.nextLine();
        
        if(nombre1.equals(nombre2)){
            System.out.println("Los nombre son iguales");
        }else{
            System.out.println("Los nombre son diferentes");
        }
  
    }
}

