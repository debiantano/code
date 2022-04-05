using System;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;
[Serializable]
class Employee
{
    int ID;
    string Name;
    public Employee(int ID, string Name)
    {
        this.ID = ID;
        this.Name = Name;
    }
}
public class Example
{
    public static void Main(string[] args)
    {
        FileStream str = new FileStream(@"C:\Users\RICHAR\Desktop\test.xml", FileMode.OpenOrCreate);
        BinaryFormatter frmtr = new BinaryFormatter();

        Employee emp = new Employee(10, "Vishal Gupta");
        frmtr.Serialize(str, emp);

        str.Close();
    }
}
