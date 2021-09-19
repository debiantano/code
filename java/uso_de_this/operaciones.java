package temporales;

public class Operaciones {
    private double radio;
    private double area;

    public Operaciones(double radio, double area) {
        this.radio = radio;
        this.area = area;
    }
    
    public Operaciones(){
        this(3,4);
    }

    public double getRadio() {
        return radio;
    }

    public void setRadio(double radio) {
        this.radio = radio;
    }

    public double getArea() {
        return area;
    }

    public void setArea(double area) {
        this.area = area;
    }
    
    
}
