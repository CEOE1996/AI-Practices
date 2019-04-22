using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using ACO.Clases;

namespace ACO
{
    class Program
    {
        static void Main(string[] args)
        {
            //Inicializacion de Variables
            int alpha = 1;
            int betha = 5;
            int Q = 100;
            int N = 30;
            int G = 10;
            double p = 0.5;
            double FInicial = 0.000001;
            Random Rand = new Random();

            //Inicializacion del Grafo
            clsGrafo Grafo = new clsGrafo("1", "4");

            clsVertice V = new clsVertice("1");
            V.Aristas.Add(new clsArista("1", "2", 5, FInicial));
            V.Aristas.Add(new clsArista("1", "3", 3.1, FInicial));
            V.Aristas.Add(new clsArista("1", "6", 5.2, FInicial));
            Grafo.Vertices.Add(V);

            V = new clsVertice("2");
            V.Aristas.Add(new clsArista("2", "1", 5, FInicial));
            V.Aristas.Add(new clsArista("2", "3", 4.9, FInicial));
            V.Aristas.Add(new clsArista("2", "7", 5.2, FInicial));
            Grafo.Vertices.Add(V);

            V = new clsVertice("3");
            V.Aristas.Add(new clsArista("3", "1", 3.1, FInicial));
            V.Aristas.Add(new clsArista("3", "2", 4.9, FInicial));
            V.Aristas.Add(new clsArista("3", "5", 6, FInicial));
            V.Aristas.Add(new clsArista("3", "6", 3.2, FInicial));
            V.Aristas.Add(new clsArista("3", "7", 3, FInicial));
            Grafo.Vertices.Add(V);

            V = new clsVertice("4");
            V.Aristas.Add(new clsArista("4", "5", 4.8, FInicial));
            V.Aristas.Add(new clsArista("4", "7", 5.5, FInicial));
            Grafo.Vertices.Add(V);

            V = new clsVertice("5");
            V.Aristas.Add(new clsArista("5", "3", 6, FInicial));
            V.Aristas.Add(new clsArista("5", "4", 5.5, FInicial));
            V.Aristas.Add(new clsArista("5", "6", 4.7, FInicial));
            Grafo.Vertices.Add(V);

            V = new clsVertice("6");
            V.Aristas.Add(new clsArista("6", "1", 5.2, FInicial));
            V.Aristas.Add(new clsArista("6", "3", 3.2, FInicial));
            V.Aristas.Add(new clsArista("6", "5", 4.7, FInicial));
            Grafo.Vertices.Add(V);

            V = new clsVertice("7");
            V.Aristas.Add(new clsArista("7", "2", 5.2, FInicial));
            V.Aristas.Add(new clsArista("7", "3", 3, FInicial));
            V.Aristas.Add(new clsArista("7", "4", 4.8, FInicial));
            Grafo.Vertices.Add(V);

            List<clsHormiga> Hormigas;
            string Recorrido;

            for(int i = 0; i < G; i++)
            {
                Hormigas = new List<clsHormiga>();

                for (int j = 0; j < N; j++)
                {
                    clsHormiga H = new clsHormiga();
                    clsVertice VerticeAnterior = new clsVertice("");
                    clsVertice VerticeActual = Grafo.getInicio();
                    double RecorridoCosto = 0;
                    Recorrido = VerticeActual.Origen;

                    while (!Grafo.isFinal(VerticeActual))
                    {
                        //Seleccion por Ruleta
                        double Sum = 0;
                        double R = Rand.NextDouble();
                        int Len = VerticeActual.Aristas.Count;
                        clsArista Camino = null;
                        double CostoVertice = 0;

                        foreach (clsArista A in VerticeActual.Aristas)
                        {
                            if (VerticeAnterior.Origen == A.Destino) { 
                                continue;
                            }

                            CostoVertice += (Math.Pow(A.Feromona, alpha) / Math.Pow(A.Costo, betha));
                        }

                        foreach (clsArista A in VerticeActual.Aristas)
                        {
                            if (VerticeAnterior.Origen == A.Destino)
                            {
                                continue;
                            }

                            Sum += (Math.Pow(A.Feromona, alpha) / Math.Pow(A.Costo, betha)) / CostoVertice;

                            if(Sum >= R)
                            {
                                Camino = A;
                                break;
                            }
                        }

                        if(Camino == null)
                        {
                            if(VerticeActual.Aristas[Len - 1].Origen == VerticeAnterior.Origen)
                            {
                                Len--;
                            }

                            Camino = VerticeActual.Aristas[Len - 1];
                        }

                        //Asigna Siguiente Vertice
                        VerticeAnterior = VerticeActual;
                        VerticeActual = Grafo.findVertice(Camino.Destino);
                        Recorrido += " - " + VerticeActual.Origen;
                        RecorridoCosto += Camino.Costo;
                        H.Visitados.Add(Camino);
                    }
                    
                    //Fin Recorrido de Hormiga
                    H.RecorridoTotal = RecorridoCosto;
                    Console.WriteLine("G: " + i + " N: " + j + " Recorrido: " + Recorrido);
                    Hormigas.Add(H);
                }

                //Deposito de Feromona
                foreach(clsVertice VG in Grafo.Vertices)
                {
                    foreach(clsArista A in VG.Aristas)
                    {
                        double Sum = 0;
                        foreach(clsHormiga H in Hormigas)
                        {
                            foreach(clsArista AH in H.Visitados)
                            {
                                if(A.Origen == AH.Origen && A.Destino == AH.Destino)
                                {
                                    Sum += Q / H.RecorridoTotal;
                                    break;
                                }
                            }
                        }

                        A.Feromona = ((1 - p) * A.Feromona) + Sum;
                    }
                }
            }
            Console.ReadKey();
        }
    }
}
