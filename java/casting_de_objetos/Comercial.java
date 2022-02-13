
package paquete1;

public class Comercial extends Empleado{
    private double comision;
  
    public Comercial(String nombre, String apellido, int edad, double salario, double comision) {
        super(nombre, apellido, edad, salario);
        this.comision=comision;
    }
     
    @Override
    public boolean plus(double plus) {
        boolean aumento = false;
        if (edad > 40 && comision > 200) {
            salario += plus;
            aumento = true;
        }
        return aumento;
    }
     
    public void metodoComercial(){
        System.out.println("Estoy en la clase comercial");
    }
}
