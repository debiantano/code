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
        Scanner entrada =new Scanner(System.in);
        
        int arreglo[] = {4,8,2,5,9};
        int dato, i=0;
        boolean flag=false;
        
        System.out.print("Digite un numero: ");
        dato = entrada.nextInt();
        
        
        while (i<5 && flag==false) {            
            if(arreglo[i]==dato){
                flag=true;
            }
            i++;
        }
        
        if (flag==false){
            System.out.println("El numero no se encuentra en el arrglo");
        }else{
            System.out.println("Numero encontrado en la posicion "+(i-1));
        }
        
    }
    
}
