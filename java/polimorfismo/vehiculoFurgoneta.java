
package paquete1;

public class vehiculoFirgoneta extends vehiculo{
    private int carga;

    public vehiculoFirgoneta(int carga, String matricula, String marca, String modelo) {
        super(matricula, marca, modelo);
        this.carga = carga;
    }

    public int getCarga() {
        return carga;
    }
    
    @Override
    public String mostrar_datos(){
        return "Marca: "+marca+"\nModelo: "+modelo+"\nMatricula: "+matricula+"\nCarga: "+carga;
    }
   
    
}
