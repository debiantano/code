using System;
using System.Runtime.InteropServices;
namespace mensaje
{
 class Program
 {
 [DllImport("user32.dll", CharSet = CharSet.Auto)]
 public static extern int MessageBox(IntPtr hWnd, String text, String caption, 
int options);
 static void Main(string[] args)
 {
 MessageBox(IntPtr.Zero, "Texto de prueba", "titulo", 0);
 }
 }
}
