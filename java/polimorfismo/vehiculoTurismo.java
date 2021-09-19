
package paquete1;

public class vahiculoTurismo extends vehiculo{
    private int nPuertas;
    
    public vahiculoTurismo(String matricula, String marca, String modelo, int nPuertas) {
        super(matricula, marca, modelo);
        this.nPuertas=nPuertas;
    }

    public int getnPuertas() {
        return nPuertas;
    }
    
    public String mostrar_datos(){
        return "Marca: "+marca+"\nModelo: "+modelo+"\nMatricula: "+matricula+"\nNPuertas: "+nPuertas;
    }
    
    
}
