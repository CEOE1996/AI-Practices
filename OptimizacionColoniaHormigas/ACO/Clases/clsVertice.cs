using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ACO.Clases
{
    public class clsVertice
    {
        public string Origen;
        public List<clsArista> Aristas;

        public clsVertice(string Origen)
        {
            this.Origen = Origen;
            Aristas = new List<clsArista>();
        }

    }
}
