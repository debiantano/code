/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package test;

import java.util.Scanner;

public class Test {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Algoritmo de Euclides");
        
        int mayor, menor;
        
        System.out.print("Numero mayor: ");
        mayor = entrada.nextInt();
        System.out.print("Numero menor: ");
        menor = entrada.nextInt();
        
        while (menor>0) {            
            if (mayor>menor) {
                mayor=mayor-menor;
            }else{
                menor=menor-mayor;
            }
        }
        System.out.println("MCD: "+ mayor);
    }
    
}
