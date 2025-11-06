#include <iostream>
#include <fstream>
using namespace std;

void flag(string dati) {
    string f = "";
    bool copia = false;

    for (size_t i = 0; i < dati.size(); i++) {
        if (dati.substr(i, 5) == "flag{")
            copia = true;
        if (copia) f += dati[i];
        if (copia && dati[i] == '}') break;
    }

    if (!f.empty())
        cout << f << endl;
    else
        cout << "Nessun flag trovato.\n";
}

int main() {
    system("ltrace -s 200 -e access -o dump.txt ./sw-10");

    ifstream file("dump.txt", ios::binary);
    string dati;
    char c;

    while (file.get(c)) {
        if (c != '\n' && c != '\r')
            dati += c;
    }

    flag(dati);
    return 0;
}
