/*
 -- estrazione flag da dump di dati -- 

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
*/

/*
    -- estrazione di png da file corrotti o modificati --

    ifstream f("dump.bin", ios::binary);
    ofstream o("flag.png", ios::binary);

    string dati((istreambuf_iterator<char>(f)), {}); // leggo tutto il dump e copio su dati

    size_t inizio = dati.find("\x89PNG\r\n\x1a\n");
    size_t fine = dati.find("IEND\xae\x42\x60\x82");

    // prendo l'indirizzo di s per l'inizio della scrittura ed estraggo il totale di byte del png 
    o.write(&dati[inizio], fine - inizio);

    cout << "PNG estratto in flag.png\n";
*/

/*
    -- funzione per spostare un dump su un'unica riga per poi estrarre con flag() -- 

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

        flag(dati);
*/