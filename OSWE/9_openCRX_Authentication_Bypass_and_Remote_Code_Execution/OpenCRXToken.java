import java.util.Random; 
 
public class OpenCRXToken { 
    public static void main(String args[]) { 
        int length = 40; 
        long start = Long.parseLong("1582038122371"); 
        long stop = Long.parseLong("1582038122769"); 
        String token = ""; 

        for (long l = start; l < stop; l++) { 
            token = getRandomBase62(length, l); 
            System.out.println(token); 
        } 
    } 
    public static String getRandomBase62(int length, long seed) { 
 
    } 
} 
