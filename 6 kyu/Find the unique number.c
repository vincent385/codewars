#include <stdio.h>
#include <stddef.h>

float finduniq(const float *nums, size_t n)
{
    // optimization issues nested for loop is too slow...
    return 0;
}

int main () {
    const float f[6] = {1, 1, 1, 2, 1, 1};
    printf("unique: %f\n", finduniq(f, 6));
    return 0;
}
