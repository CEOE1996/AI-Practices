using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ACO.Clases
{
    public class clsArista
    {
        public string Origen;
        public string Destino;
        public double Costo;
        public double Feromona;

        public clsArista(string Origen, string Destino, double Costo, double Feromona)
        {
            this.Origen = Origen;
            this.Destino =Destino;
            this.Costo = Costo;
            this.Feromona = Feromona;
        }
    }
}
