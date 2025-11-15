#include <iostream>

int main(){
    system("objdump -h sw-03");
    system("xxd -s 0x3043 -l 0x1c sw-03");
    return 0;
}