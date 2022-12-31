#include <stdlib.h>

typedef unsigned long long ull;

ull *genfib(int n);

ull perimeter(int n) {
    ull *seq = genfib(n);
    ull sum = 0;
    for (int i = 0; i < n + 2; i++) sum += seq[i];
    free(seq);
    return 4*sum;
}

ull *genfib(int n) {
    if (n == 0)
        return NULL;
    ull *seq = malloc((n+2) * sizeof(ull));
    seq[0] = 0;
    seq[1] = 1;
    for (int i = 2; i < n + 2; i++) seq[i] = seq[i - 1] + seq[i - 2];
    return seq;
}
