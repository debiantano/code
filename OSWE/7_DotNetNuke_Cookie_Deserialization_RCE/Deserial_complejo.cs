using System; 
using System.Diagnostics; 
using System.IO; 
using System.Xml; 
using System.Xml.Serialization;

namespace MultiXMLDeserializer 
{ 
    class Program 
    { 
        static void Main(string[] args) 
        { 
            String xml = File.ReadAllText(args[0]); 
            CustomDeserializer(xml); 
        }
        
        static void CustomDeserializer(String myXMLString)
        { 
            XmlDocument xmlDocument = new XmlDocument(); 
            xmlDocument.LoadXml(myXMLString);

            foreach (XmlElement xmlItem in xmlDocument.SelectNodes("customRootNode/item")) 
            {
                string typeName = xmlItem.GetAttribute("objectType");
                var xser = new XmlSerializer(Type.GetType(typeName));
                var reader = new XmlTextReader(new 
                StringReader(xmlItem.InnerXml)); 
                xser.Deserialize(reader); 
            } 
        } 
    } 
}

