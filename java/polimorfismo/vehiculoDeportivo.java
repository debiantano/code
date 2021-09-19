
package paquete1;

public class vehiculoDeportivo extends vehiculo{
    private int cilindrada;

    public vehiculoDeportivo(String matricula, String marca, String modelo, int cilindrada){
        super(matricula, marca, modelo);
        this.cilindrada=cilindrada;
    }

    public int getCilinrada(){
        return cilindrada;
    }
    
    @Override
    public String mostrar_datos(){
        return "Marca: "+marca+"\nModelo: "+modelo+"\nMatricula: "+matricula+"\nCilindrada: "+cilindrada;
    }
}
