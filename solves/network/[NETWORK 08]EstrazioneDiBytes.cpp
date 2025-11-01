#include <iostream>

using namespace std;

void flag(string dati) {
    string f = "";
    bool copia = false;

    for (int i = 0; i < dati.size(); i++) {
        if (dati[i] == 'f' && dati.substr(i, 5) == "flag{") {
            copia = true;
        }
        if (copia) f += dati[i];
        if (dati[i] == '}') break;
    }

    cout << f;
}

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
