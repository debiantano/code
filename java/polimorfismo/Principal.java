package paquete1;

public class principal {
    public static void main(String[] args) {
        vehiculo misVehiculos[]=new vehiculo[4];
        
        misVehiculos[0]=new vehiculo("GH76","Ferrari","A89");
        misVehiculos[1]=new vahiculoTurismo("GH45", "Audi", "P15", 4);
        misVehiculos[2]=new vehiculoDeportivo("AW81", "toyota", "GFI", 500);
        misVehiculos[3]=new vehiculoFirgoneta(2000, "J18", "Toyota", "J9");
        
        for(vehiculo vehiculos:misVehiculos){
            System.out.println(vehiculos.mostrar_datos());
            System.out.println("");
        }
    }
}
