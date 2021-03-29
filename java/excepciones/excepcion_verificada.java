
package temporales;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

public class errores {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        // EXCEPCIONES VERIFICADAS (IOException)
        //java te obliga a solucionarlas
        
        // LECTURA DE UN ARCHIVO DE TEXTO
         BufferedReader bf = new BufferedReader(new FileReader("d:\\test.txt"));
         String cadena;
         
         while((cadena = bf.readLine()) != null){
             System.out.println(cadena);
         }
         
    }
}
