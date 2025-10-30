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
    string dati = "flag{Y0u_kn0w_Wh4t_a_Pc4p_1s}";
    flag(dati);
}
