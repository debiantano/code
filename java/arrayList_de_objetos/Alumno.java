
package temporales;

import java.text.SimpleDateFormat;
import java.util.Date;

public class Alumno {
    private String nombre;
    private int edad;
    private Date fecha;
    private int dni;

    public Alumno(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }
    
    public Alumno(String nombre, int edad, Date fecha, int dni) {
        this.nombre = nombre;
        this.edad = edad;
        this.fecha = fecha;
        this.dni = dni;
    }
    
    // FORMATO FHCHA
    
    public String formato_fecha(){
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
        String fechaFormateada = sdf.format(fecha);
        return fechaFormateada;
    }

    @Override
    public String toString() {
        return "Alumno{" + "nombre=" + nombre + ", edad=" + edad + ", fecha=" + fecha + ", dni=" + dni + '}';
    } 
}
