#include <stdio.h>
#include <stdlib.h>

// Basically fibonacci but sums last 3 numbers of the sequence to generate the next instead of the last 2
long long *tribonacci(const long long signature[3], size_t n) {
    if (n == 0)
        return NULL;
    long long *seq = (long long *) malloc(n * sizeof(long long));
    seq[0] = signature[0];
    seq[1] = signature[1];
    seq[2] = signature[2];
    for (size_t i = 3; i < n; i++) {
        seq[i] = seq[i - 1] + seq[i - 2] + seq[i - 3];
    }
    return seq;
}
