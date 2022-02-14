using System;
using System.Collections;
using System.Collections.Generic;

namespace POO
{

     class Program
    {
        static void Main(string[] args)
        {
            // LISTA 1
            ArrayList lista = new ArrayList();

            lista.Add(1203);
            lista.Add("test123");
            lista.Add(1.23);

            foreach(var i in lista)
            {
                Console.WriteLine(i.ToString());
            }

            
            // LISTA 2
            List<int> lista2 = new List<int>();
            lista2.Add(1);
            lista2.Add(2);
            lista2.Add(3);

            foreach(var dato in lista2)
            {
                Console.WriteLine(dato.ToString());
            }
        }
    }
}
