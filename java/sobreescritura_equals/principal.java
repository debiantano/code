
package temporales;

public class principal {
    public static void main(String[] args) {
    Punto punto1 = new Punto(10, 2);
    Punto punto2 = new Punto(10, 2);
    Punto punto3 = new Punto(20, 4);
    
    if(punto1.equals(punto2)){
        System.out.println("verdadero");
    }else{
        System.out.println("falso");
    }
    if (punto1.equals(punto3))
            System.out.println("verdadero");
    else
            System.out.println("falso");
    }
  
}
