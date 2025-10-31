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
    string dati = "GET / HTTP/1.1 Host: pwn.flag.org User-Agent: curl/7.64.0 Accept: */ Flag-String: flag{L3aRn1N9_4b0uT_F1lter5_p1}";
    flag(dati);
}
