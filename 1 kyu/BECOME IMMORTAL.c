#include <stdio.h>

unsigned elderAge(unsigned m, unsigned n, unsigned l, unsigned t) {
    unsigned sum = 0;
    for (unsigned i = 0; i < n; i++) {
        for (unsigned j = 0; j < m; j++) {
            if ((i^j) - l >= l)
                sum += (i^j) - l;
        }
    }
    printf("%u\n", sum);
    if (sum < t)
        return sum;
    return sum - t;
}

int main() {
    printf("%u\n", elderAge(8, 5, 1, 100));
    return 0;
}
