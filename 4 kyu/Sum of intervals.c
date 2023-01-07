#include <stddef.h>

struct interval {
    int first;
    int second;
};

int sum_intervals(const struct interval *v, size_t n)
{
    int sum = 0;
    for (size_t i = 0; i < n; i++) {
        sum += (v+i)->second - (v+i)->first;
    }
    return sum;
}
