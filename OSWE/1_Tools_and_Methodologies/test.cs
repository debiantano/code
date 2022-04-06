using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace debbug
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Tu lenguaje favorito: ");
            string answer = Console.ReadLine();
            Console.WriteLine("\n[+] Tu lenguaje favorito es: " + answer + "\r\n");
        }
    }
}
