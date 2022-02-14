using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace POO
{
     class Program
    {
        static void Main(string[] args)
        {
            // CREAR INSTANCIA
            ventana calculadora = new ventana();
            calculadora.cerrar();
            calculadora.maximizar();

            Console.ReadKey();

        }
    }

    class ventana
    {
        // ATRIBUTOS
        public int edad;          // publico
        private string color;    // solo desde esta clase
        static string name;      // variable sincronizado
        protected int ancho;     // solo las instancias de clases derivadas
        
        // METODOS
        public void cerrar()
        {
            Console.WriteLine("La ventana se cerró");
        }
        
        private void minimizar()
        {
            Console.WriteLine("La ventana se minimizó");
        }

        public void maximizar()
        {
            Console.WriteLine("La ventana se maximizó");
        }

    }
}
