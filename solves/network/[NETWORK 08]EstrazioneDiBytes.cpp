#include <iostream>
using namespace std;

int main() {

    /*
    filtrare con ip.src == 192.168.100.1 && ip.dst == 192.168.100.2 && tcp
    estrarre data in 'dump.gz' (1f8b08 indica che è un .gz)
    */ 
    
    // su windows
    system("tar -xvzf output.gz");
    cout << "Flag: ";
    system("type flag.txt");


    return 0;
}
