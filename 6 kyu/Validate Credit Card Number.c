#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int *digits2arr(long digits);

bool validate(long digits)  {
    int *digitArr = digits2arr(digits);
    return false;
}

int main () {
    printf("the number %d is %s\n", 1324, validate(1324) ? "valid" : "invalid");
    return 0;
}

int getDigitCount(long digits) {
    int n = 0;
    while (digits) {
        digits /= 10;
        n++;
    }
    return n;
}

int *digits2arr(long digits) {
    int n = getDigitCount(digits);
    int *arr = malloc(n * sizeof(int));
    size_t i = 0;
    while (digits) {
        arr[i] = digits % 10;
        digits /= 10;
        i++;
    }
    return arr;
}
