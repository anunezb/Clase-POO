using System;

namespace EjdeRepaso
{
    class Program
    {
        static double FunPago(char nivel, int horas)
        {
            double pago;

            switch (nivel)
            {
                case 't':
                    pago = horas * 500;
                    break;
                case 'j':
                    pago = horas * 800;
                    break;
                case 's':
                    pago = horas * 1000;
                    break;
                default:
                    break;
            }
            
            return pago; 
        }

        static void Main(string[] args)
        {
            // Ejercicio 1

            // Variables
            char nivel;
            int horas;

            // Operaciones
            for (int i = 0; i < 3; i++)
            {
                do
                {
                    Console.Write("Nivel: ");
                    nivel = char.Parse(Console.ReadLine());
                    nivel = char.ToLower(nivel);
                } while (nivel != 't' && nivel != 'j' && nivel != 's');

                Console.Write("Horas trabajadas: ");
                horas = int.Parse(Console.ReadLine());

                Console.WriteLine("Se le debe pagar" + FunPago(nivel, horas));
            }
            




            /* Ejercicio 2
            // Variables
            int[] numeros = new int[100000];
            int multiplos = 7;

            // Operaciones
            for (int i = 0; multiplos <= 5000; i+=7)
            {
                numeros[i] = multiplos;
                if (numeros[i] % 3 == 0)
                {

                }
                

                
            }
            */

        }
    }
}
