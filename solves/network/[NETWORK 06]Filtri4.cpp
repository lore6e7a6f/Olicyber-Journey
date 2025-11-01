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

    // filtrare con frame contains "Pwn all the things!!!"

    string dati = "Pwn all the things!!! the fl4g is: flag{L3aRn1N9_4b0uT_F1lter5_F1nd_Th0s3_Str1n65_m8}";
    flag(dati);
    return 0;
}
