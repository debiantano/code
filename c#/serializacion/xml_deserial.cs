using System.Xml.Serialization;
using System.IO;
using System;

namespace serialization
{
    class Program
    {
        static void Main(string[] args)
        {
            // Construct an instance of the XmlSerializer with the type of object that is being deserialized.
            var mySerializer = new XmlSerializer(typeof(Employee));
            // To read the file, create a FileStream.
            var myFileStream = new FileStream(@"C:\Users\RICHAR\Desktop\Serialization.xml", FileMode.Open);
            // Call the Deserialize method and cast to the object type.
            var myObject = (Employee)mySerializer.Deserialize(myFileStream);
            Console.WriteLine(myObject.Id);
            Console.WriteLine(myObject.name);
            Console.WriteLine(myObject.subject);
        }
    }
    public class Employee
    {
        public int Id = 1;
        public string name = "John Smith";
        public string subject = "Physics";
    }
}


