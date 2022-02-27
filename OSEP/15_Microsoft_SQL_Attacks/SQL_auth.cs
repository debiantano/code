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
                Console.WriteLine("Auth success!");
            }
            catch
            {
                Console.WriteLine("Auth failed");
                Environment.Exit(0);
            }
            con.Close();
        }

    }
}
