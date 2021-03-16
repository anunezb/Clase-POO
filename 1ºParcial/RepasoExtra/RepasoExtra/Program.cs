using System;

namespace RepasoExtra
{
    class Program
    {
        static void Promedio(int[,] m)
        {
            int suma = 0;
            double prom;
            for (int col = 0; col < 2; col++)
            {
                for (int ren = 0; ren < 3; ren++)
                {
                    suma = suma + m[ren, col];
                    prom = suma / 3;
                    Console.WriteLine("Promedio renglón 1: " + prom);
                }
            }
        }

        static void Main(string[] args)
        {
            int[,] m = new int[3, 2];

            for (int col = 0; col < 2; col++)
            {
                for (int ren = 0; ren < 3; ren++)
                {
                    Console.Write("Número" + ren + "," + col + ": ");
                    m[ren,col] = int.Parse(Console.ReadLine());
                }
            }
            Promedio(m);
        }
    }
}
