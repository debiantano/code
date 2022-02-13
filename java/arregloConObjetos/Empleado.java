
package paquete1;


public class Empleado {
    private String nombre;
    private int edad;
    private float sueldo;
    
    public Empleado(String nombre, int edad, float sueldo) {
        this.nombre = nombre;
        this.edad = edad;
        this.sueldo = sueldo;
    }

    @Override    
    public String toString(){
        return nombre+", "+edad+", "+sueldo;
    }
    
}
