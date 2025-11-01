#include <iostream>
#include <fstream>
#include <string>

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
    filtrare con 'frame contains data && tcp'
    -> follow tcp stream -> salvare file come dump.txt
    */ 
    
    string dati;
    ifstream file("dump.txt", ios::binary);

    if (!file) {
        cout << "Errore apertura file\n";
        return 1;
    }

    char c;
    while (file.get(c)) {
        if (c != '\n' && c != '\r')  // ignora newline e carriage return
            dati += c;
    }

    file.close();

    // cout << dati;  debug

    flag(dati);
    return 0;
}
