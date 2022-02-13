/* Diseñar un programa para trabajar con los triangulos isosceles.Para ello defina los atributos necesarios que se requieren, 
proporcione métodos de consulta, un método constructor e implemente métodos para calcular el perímetro y el área de un triángulo,
además implementar un método que a partir de un arreglo de triángulos devuelva el área del triángulo de mayor superficie.
*/
package paquete1;

import java.util.Scanner;

public class principal {
    public static float mayorArea(triangulo triangulos[]){
        float area;
        
        area=triangulos[0].obtener_area();
        
        for(int i=0;i<triangulos.length;i++){
            if(triangulos[i].obtener_area()>area){
                area=triangulos[i].obtener_area();
            }
        }
        return area;
    }
    
    public static void main(String[] args) {
        Scanner entrada= new Scanner(System.in);
        float base,lado;
        int nTriangulos;
        
        System.out.print("Digite el numero de triangulos a ingresar: ");
        nTriangulos=entrada.nextInt();
        
        triangulo triangulos[] = new triangulo[nTriangulos];
        
        for (int i = 0; i < triangulos.length; i++) {
            System.out.println("Digite los valores para el triangulo "+(i+1)+" : ");
            System.out.print("Introduce la base: ");
            base=entrada.nextFloat();
            System.out.print("Introduce un lado: ");
            lado=entrada.nextFloat();
            
            triangulos[i]= new triangulo(lado,base);
    
            System.out.println("El perimetro del triangulo es: "+triangulos[i].obtener_perimetro());
            System.out.println("El area del triangulo es: "+triangulos[i].obtener_area());
        }
        
        System.out.println("Triangulo con mayor area es: "+principal.mayorArea(triangulos));
        
   }
    
}
