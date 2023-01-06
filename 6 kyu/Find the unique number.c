#include <stddef.h>

float finduniq(const float *nums, size_t n)
{
    if (nums[0] != nums[1])
        if (nums[0] != nums[2])
            return nums[0];
        else
            return nums[1];
    else {
        for (size_t i = 2; i < n; i++) {
            if (nums[i] != nums[0])
                return nums[i];
        }
    }
}
