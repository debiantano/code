package temporales;

import java.text.SimpleDateFormat;
import java.util.Date;

public class Temporales {

    public static void main(String[] args) {
        Date fechaActual=new Date();
        
        SimpleDateFormat sdf=new SimpleDateFormat("dd/MM/yyyy");
        SimpleDateFormat sdf2=new SimpleDateFormat("dd-MM-yyyy");
        
        String fechaFormateada=sdf.format(fechaActual);
        String fechaFormateada2=sdf2.format(fechaActual);
        
        System.out.println(fechaFormateada);
        System.out.println(fechaFormateada2);
        System.out.println();
    }  
}
