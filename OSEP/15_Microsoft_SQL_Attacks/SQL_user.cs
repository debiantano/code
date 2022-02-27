// Inicio de sesión, nombre de usuario y membresías de roles
using System;
using System.Data.SqlClient;
namespace SQL
{
    class Program
    {
        static void Main(string[] args)
        {
            String sqlServer = "COMPUTER";
            String database = "master";
            String conString = "Server = " + sqlServer + "; Database = " + database +"; Integrated Security = True;";

            SqlConnection con = new SqlConnection(conString);
            try
            {
                con.Open();
                Console.WriteLine("[+]Éxito de autenticación!");
            }
            catch
            {
                Console.WriteLine("[!] Autenticación fallida");
                Environment.Exit(0);
            }

            String querylogin = "SELECT SYSTEM_USER;";
            SqlCommand command = new SqlCommand(querylogin, con);
            SqlDataReader reader = command.ExecuteReader();

            reader.Read();
            Console.WriteLine("[+] Conectado como: " + reader[0]);
            reader.Close();

            String querypublicrole = "SELECT IS_SRVROLEMEMBER('public');";
            command = new SqlCommand(querypublicrole, con);
            reader = command.ExecuteReader();
            reader.Read();
            Int32 role = Int32.Parse(reader[0].ToString());
            if (role == 1)
            {
                Console.WriteLine("[+] El usuario es miembro del rol público");
            }
            else
            {
                Console.WriteLine("[!] El usuario NO es miembro del rol público");
            }
            reader.Close();

            con.Close();
        }

    }
}
