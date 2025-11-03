#include <iostream>
using namespace std;

int main() {
    // flag bytes (14)
    const unsigned char flag[] = {
        0xD4, 0x5C, 0xDC, 0xBB, 0x6B, 0x1E, 0xD3, 0x4A,
        0x4A, 0x5E, 0xD2, 0xDF, 0xAC, 0x7C
    };

    // key bytes (14)
    const unsigned char key[] = {
        0xB2, 0x30, 0xBD, 0xDC, 0x10, 0x7A, 0xE1, 0x7B,
        0x2C, 0x3B, 0xE2, 0xEC, 0x99, 0x01
    };

    const int N = 14;
    unsigned char output[N];
    
    // XOR 
    for (int i = 0; i < N; ++i) {
        output[i] = flag[i] ^ key[i];
    }

    for(int i=0;i<14;i++){
        cout << output[i];
    }
    
    return 0;
}
