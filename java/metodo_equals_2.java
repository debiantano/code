package temporales;

import java.util.Scanner;
import javax.swing.JOptionPane;


public class principal {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        String user, password;
        
        System.out.print("Ingrese su nombre de usuario: ");
        user=entrada.nextLine();
        System.out.print("Ingrese su contraseña: ");
        password=entrada.nextLine();
        
        if(user.equals("admin") && password.equals("mypass123")){
            System.out.println("Inicio de sesion correcto");
        }else{
            System.out.println("Nombre de usuario o contraseña incorrecta");
        }
        
    }
}
