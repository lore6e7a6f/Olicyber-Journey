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
    Edit -> Preferences -> Protocols -> TLS -> (Pre)-Master-Secret log filename -> inserire il .txt
    filtrare con http2.headers
    */

    string dati = "flag{S3cr3t_K3y5_4re_n0_J0k3}";
    flag(dati);
    return 0;
}
