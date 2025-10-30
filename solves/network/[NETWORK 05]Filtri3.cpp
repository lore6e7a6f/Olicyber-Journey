#include <iostream>
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

    // filtrare con frame.comment

    string dati = "Wow, so you can also save comments! Not so easy to find, or maybe it is?! :\ flag{L3aRn1n9_4b0uT_F1lter5_C0mm3Nt5_4R3_H4rd_t0_f1nD}";
    flag(dati);
    return 0;
}
