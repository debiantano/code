
package temporales;

public class Punto {
    
    private int x, y;

    public Punto(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public boolean equals(Object obj) {
        Punto punto = (Punto) obj;
        System.out.println(x);
        System.out.println(y);
        if (x==punto.x && y== punto.y)
            return true;
        else
            return false;
    }
    
    
}
