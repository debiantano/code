//serial.exe "Hello AWAE"
using System;
using System.IO; 
using System.Xml.Serialization;

namespace BasicXMLSerializer 
{ 
    class Program 
    {
        static void Main(string[] args) 
        { 
            MyConsoleText myText = new MyConsoleText();
            myText.text = args[0];
            MySerializer(myText); 
        }
        static void MySerializer(MyConsoleText txt) 
        { 
            var ser = new XmlSerializer(typeof(MyConsoleText));
            TextWriter writer = new StreamWriter("C:\\Users\\RICHAR\\Desktop\\basicXML.txt");
            ser.Serialize(writer, txt);
            writer.Close(); 
        } 
    }

    public class MyConsoleText
    { 
        private String _text;
        public String text 
        { 
            get { return _text; } 
            set { _text = value; Console.WriteLine("Mi primera clase de texto de consola dice: " + _text); }
        } 
    } 
}

