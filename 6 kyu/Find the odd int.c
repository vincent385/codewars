#include <stddef.h>

// From an array of integers, find the one that appears an odd number of times.
int find_odd (size_t length, const int array[length])
{
    for (int i = 0; i < length; i++) {
        int count = 0;
        for (int j = 0; j < length; j++) {
            if (array[i] == array[j])
                count++;
        }
        if (count % 2 != 0)
            return array[i];
    }
}
