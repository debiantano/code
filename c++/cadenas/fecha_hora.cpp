#include <iostream> 
#include <time.h>
 
using namespace std;

 const string currentDateTime() {
	time_t now = time(0);
	struct tm tstruct;
	char buf[80];
	tstruct = *localtime(&now);
	// for more information about date/time format 
	strftime(buf, sizeof(buf), "Fecha: %Y-%m-%d\t\tHoha: %X", &tstruct);
	return buf;
	}
int main() {
	cout<<currentDateTime() <<"test123"<<endl;
	return 0;
}

