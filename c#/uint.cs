using System;

namespace Geeks
{
	class test
	{
		static void Main(string[] args)
		{
			uint num = 24680;

			// TIPO DE VARIABLE
			Console.WriteLine("Tipo de variable           : " + num.GetType());

			// IMPRIMIR VALOR
			Console.WriteLine("numero                     : " + num);

			// IMPRIMIR TAMAÑO
			Console.WriteLine("Tamaño de una variable uint: " + sizeof(uint));

			// MINIMO Y MAXIMO VALOR DE UINT
			Console.WriteLine("Valor mínimo de uint       : " + uint.MinValue);
			Console.WriteLine("Valor máximo de uint       : " + uint.MaxValue);

			Console.ReadLine();
		}
	}
}
