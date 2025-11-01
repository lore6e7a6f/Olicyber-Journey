#include <iostream>
#include <fstream>

using namespace std;

int main() {

    /*
    File -> Esporta oggetti -> HTTP -> Frame 10 -> salva come "dump.bin"
    */

    ifstream f("dump.bin", ios::binary);
    ofstream o("flag.png", ios::binary);

    string dati((istreambuf_iterator<char>(f)), {}); // leggo tutto il dump e copio su dati

    size_t inizio = dati.find("\x89PNG\r\n\x1a\n");
    size_t fine = dati.find("IEND\xae\x42\x60\x82");

    // prendo l'indirizzo di s per l'inizio della scrittura ed estraggo il totale di byte del png 
    o.write(&dati[inizio], fine - inizio);

    cout << "PNG estratto in flag.png\n";
    
}
