package temporales;

import javax.swing.JOptionPane;


public class Temporales {

    public static void main(String[] args) {
        int n1=Integer.parseInt(JOptionPane.showInputDialog("Digite un numero:"));
        int n2=Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero:"));
        
        Operaciones op1=new Operaciones();
        int suma=op1.sumar(n1,n2);
        int resta=op1.restar(n1,n2);
        int mult=op1.multiplicar(n1, n2);
        int div=op1.dividir(n1, n2);
        
        op1.mostrarResultados(suma,resta,mult,div);


    }  
}
