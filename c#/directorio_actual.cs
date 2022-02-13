using System;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
		      String dir = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments);
	        Console.WriteLine(dir);

        }
    }
}
