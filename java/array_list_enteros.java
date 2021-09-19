
package temporales;

import java.util.ArrayList;

public class Array_list {
    public static void main(String[] args) {
        ArrayList<Integer> numeros = new ArrayList<Integer>();
        numeros.add(12);
        numeros.add(13);
        numeros.add(14);
        numeros.add(15);
        System.out.println("Cantidad de numeros: "+ numeros.size());
        
        for(int i=0;i<numeros.size();i++){
            System.out.println(numeros.get(i));
        }
    }
}
