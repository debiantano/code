package temporales;

public class Operaciones {
    
    
    public int sumar(int num1, int num2){
        int suma=num1+num2;
        return suma;
    }
    
    public int restar(int num1, int num2){
        int resta=num1-num2;
        return resta;
    }
    
    public int multiplicar(int num1, int num2){
        int multiplicacion=num1*num2;
        return multiplicacion;
    }
    
    public int dividir(int num1, int num2){
        int division=num1/num2;
        return division;
    }
    public void mostrarResultados(int suma, int resta, int multiplicacion, int division){
        System.out.println("la suma es "+suma);
        System.out.println("La resta es: "+resta);
        System.out.println("La multiplicacio es: "+multiplicacion);
        System.out.println("La division es: "+division);
    }
    
}
