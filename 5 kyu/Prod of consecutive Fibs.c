#include <stdlib.h>

typedef unsigned long long ull;

unsigned long long* productFib(ull prod) {
    ull *ret = malloc(3 * sizeof(long long));
    long a = 0;
    long b = 1;
    while (a*b < prod) {
        b = b + a;
        a = b - a;
    }
    ret[0] = a;
    ret[1] = b;
    ret[2] = a*b == prod;
    return ret;
}
