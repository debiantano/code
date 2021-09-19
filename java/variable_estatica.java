
package temporales;

public class principal {
    public static void main(String[] args) {
        Estudiante s1 = new Estudiante();    
        s1.showData();    
        Estudiante s2 = new Estudiante();    
        s2.showData();
    }
}

class Estudiante{
    int a;
    static int b;

    public Estudiante() {
    b++;
    }
    
    public void showData(){
        System.out.println("a ="+a);
        System.out.println("b = "+b);
    }
}
