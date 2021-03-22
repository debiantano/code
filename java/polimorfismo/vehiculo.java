
package paquete1;

public class vehiculo {
    protected String matricula;
    protected String marca;
    protected String modelo;

    public vehiculo(String matricula, String marca, String modelo) {
        this.matricula = matricula;
        this.marca = marca;
        this.modelo = modelo;
    }

    public String getMatricula() {
        return matricula;
    }

    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }
    
    public String mostrar_datos(){
        return "Marca: "+marca+"\nModelo: "+modelo+"\nMatricula: "+matricula;
    }
    
}
