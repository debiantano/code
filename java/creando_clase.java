
package ClasesYObjetos;

public class Coche {
    // ATRIBUTOS
    String color;
    String marca;
    int km;
    
    //METODOS
    public static void main(String [] args){
        Coche coche1=new Coche();
        
        coche1.color="blanco";
        coche1.marca="toyota";
        coche1.km=0;
        
        System.out.println(coche1.color);
        System.out.println(coche1.marca);
        System.out.println(coche1.km);
        
        Coche coche2=new Coche();
        
        coche2.color="negro";
        coche2.marca="Ferrary";
        coche2.km=100;
        
        System.out.println("\n"+coche2.color);
        System.out.println(coche2.marca);
        System.out.println(coche2.km);
        
    } 
}
