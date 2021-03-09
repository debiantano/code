
package paquete1;

public class Principal {
    public static void main(String [] args){
        Empleado array[] = {
            new Empleado("bob", 12, 12.4f),
            new Empleado("calamardo", 11, 12.2f),
            new Empleado("arenita", 13, 54.34f),
            new Empleado("patricio", 14, 654.2f)};
    
        for (int i=0;i<array.length;i++){
            System.out.println(array[i]);
        }
        
        // LONGITUD DE UN ARRAY
        System.out.println("Longitud: "+array.length);
    }
    
}
