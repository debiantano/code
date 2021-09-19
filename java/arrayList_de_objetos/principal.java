
package temporales;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

public class Array_list {
    public static void main(String[] args) {
        ArrayList<Alumno> listaDeAlumnos = new ArrayList<Alumno>();
        Alumno al1 = new Alumno("uno", 12);
        Alumno al2 = new Alumno("dos", 24);
        
        listaDeAlumnos.add(al1);
        listaDeAlumnos.add(al2);
        
        for(int i=0;i<listaDeAlumnos.size();i++){
            System.out.println(listaDeAlumnos.get(i));
        }
    
        System.out.println("\n");
        
        for(Alumno a : listaDeAlumnos){
            System.out.println(a.toString());
        }
        
        
    }
}
