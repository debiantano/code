package temporales;

import java.text.SimpleDateFormat;
import java.util.Date;

public class Temporales {

    public static void main(String[] args) {
        Date fechaActual=new Date();
        
        SimpleDateFormat sdf=new SimpleDateFormat("dd/MM/yyyy");
        SimpleDateFormat sdf2=new SimpleDateFormat("dd-MM-yyyy");
        String fechaFormateada=sdf.format(fechaActual);
        
        System.out.println(fechaFormateada);
        System.out.println();
    }  
}
