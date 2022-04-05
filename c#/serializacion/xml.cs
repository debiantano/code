using System.Xml.Serialization;  
using System.IO;  

namespace serialization
{
    class Program
    {
        static void Main(string[] args)
        {
            Employee bs = new Employee();
            XmlSerializer xs = new XmlSerializer(typeof(Employee));
            TextWriter txtWriter = new StreamWriter(@"C:\Users\RICHAR\Desktop\Serialization.xml");
            xs.Serialize(txtWriter, bs);
            txtWriter.Close();

        }
    }
    public class Employee
    {
        public int Id = 1;
        public string name = "John Smith";
        public string subject = "Physics";
    }
}
