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

    // filtrare con ip.src=192.168.100.3 && dns

    string dati = "···  ·      *flag{L3aRn1N9_4b0uT_F1lter5_1P_DN5_f1lt3r} · ·";
    flag(dati);
    return 0;
}
