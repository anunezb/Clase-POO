using System;

namespace Matrices
{
    class Program
    {
        static void Promedio_Mensual(double[,] datos)
        {
            double[] promedio = new double[10];
            for (int i = 0; i < 12; i++)
            {
                for (int j = 0; j < 10; j++)
                {
                    promedio[j] += datos[i, j];
                }
                promedio[j] /= 10;
            }
            Console.WriteLine(promedio.Min());
        }

        static void Promedio_Años(double[,] datos)
        {
            double[] suma = new double[10];
            for (int i = 0; i < 10; i++)
            {
                for (int j = 0; j < 12; j++)
                {
                    suma[j] += datos[j, i];
                }
                
            }
            Console.WriteLine(suma.Max());
        }

        static void Minimo_Total(double[,] datos)
        {
            int[] gastos = new int[120];
            int n = 0;

            for (int i = 0; i < 10; i++)
            {
                for (int j = 0; j < 12; j++)
                {
                    gastos[n] = datos[i, j];
                    n++;
                }
            }

        }

        static void Main(string[] args)
        {
            // Eje 1 Matriz gastos años y meses

            // Declaración de matriz

            double[,] datos = new double[10, 12];

            for (int i = 0; i < 10; i++)
            {
                for (int j = 0; j < 12; j++)
                {
                    Console.Write("Ingresa la ganancia del mes " + (j + 1) + " del año " + (i + 1));
                    datos[i, j] = double.Parse(Console.ReadLine());
                }
            }

            Promedio_Mensual(datos);
            Promedio_Años(datos);

            //



        }
    }
}
