#include <stdio.h>
#include <stddef.h>

float finduniq(const float *nums, size_t n)
{
    size_t i = 0;
    size_t j = 0;
    int count = 0;
    while (i < n) {
        if (nums[i] == nums[j])
            count++;
        if (j % n == 0 && j != 0) {
            if (count == 1)
                break;
            i++;
            j = 0;
            count = 0;
        }
        j++;
    }
    return nums[i];
}

int main () {
    const float f[6] = {1, 1, 1, 2, 1, 1};
    printf("unique: %f\n", finduniq(f, 6));
    return 0;
}
