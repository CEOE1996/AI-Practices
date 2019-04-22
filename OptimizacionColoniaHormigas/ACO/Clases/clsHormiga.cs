using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ACO.Clases
{
    public class clsHormiga
    {
        public List<clsArista> Visitados;
        public double RecorridoTotal;

        public clsHormiga()
        {
            Visitados = new List<clsArista>();
            RecorridoTotal = 0;
        }
    }

}
