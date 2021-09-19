
package paquete1;

public class triangulo {
    private float lado;
    private float base;

    public triangulo(float lado, float base) {
        this.lado = lado;
        this.base = base;
    }

    public void triangulo(float lado,float base){
        this.lado=lado;
        this.base=base;
    }
    
    public float obtener_perimetro(){
        float perimetro;
        perimetro=(2*lado)+base;
        return perimetro;
    }
    
    public float obtener_area(){
        float area;
        area=(float)((base*Math.sqrt(lado*lado-(base*base)/4))/2);
        return area;
    }

    public String mostrar_datos(){
        return "Base: "+base+"\nLado: "+"\nPerimetro: "+obtener_perimetro()+"\nArea: "+obtener_area();
    }
}
