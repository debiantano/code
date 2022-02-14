using System;

namespace ESTRUCTURAS
{
    struct celulares
    {
        public int memoria;
        public string marca;
        public string modelo;
    }
     class Program
    {
        static void Main(string[] args)
        {
            celulares cel;

            cel.memoria = 12;
            cel.marca = "sony";
            cel.modelo = "zzc";

            Console.WriteLine("Memoria de: " + cel.memoria);

            Console.ReadKey();

        }
    }
}
