using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ACO.Clases
{
    public class clsGrafo
    {
        public List<clsVertice> Vertices;
        public string Inicio;
        public string Fin;

        public clsGrafo(string Inicio, string Fin)
        {
            Vertices = new List<clsVertice>();
            this.Inicio = Inicio;
            this.Fin = Fin;
        }

        public clsVertice getInicio() {
            foreach(clsVertice V in Vertices)
            {
                if(V.Origen == Inicio)
                {
                    return V;
                }
            }

            return new clsVertice("");
        }

        public clsVertice findVertice(string Vertice)
        {
            foreach (clsVertice V in Vertices)
            {
                if (V.Origen == Vertice)
                {
                    return V;
                }
            }

            return new clsVertice("");
        }

        public bool isFinal(clsVertice V)
        {
            if(V.Origen == Fin)
            {
                return true;
            }
            return false;
        }

    }
}
