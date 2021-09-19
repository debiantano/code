package temporales;

import javax.swing.JOptionPane;


public class Temporales {

    public static void main(String[] args) {
        int resultado=1;
        // producto de los 10 primeros numeros impares
        for(int i=1;i<=20;i+=2){
            resultado*=i;
        }
        System.out.println("El producto es: "+resultado);

    }  
}
