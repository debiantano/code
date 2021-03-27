
package temporales;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

public class Fecha_java {
    
    public static SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/YYYY");
    public static SimpleDateFormat sdf2 = new SimpleDateFormat("dd-MMM-YYYY");
    
    public static String dateString(Date fecha){
        return sdf.format(fecha);
    }
    public static String dateString2(Date fecha){
        return sdf2.format(fecha);
    }

    public static void main(String[] args) {    
        Date fechaActual = new Date();
        Date fechaActual2 = new Date();
        
        System.out.println(dateString(fechaActual));
        System.out.println(dateString2(fechaActual));
    }
}
