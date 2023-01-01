#include <stdlib.h>
#include <stdbool.h>

int getDigitCount(long digits);
int *digits2arr(long digits, int length);

bool validate(long digits)  {
    int n = getDigitCount(digits);
    int *digitArr = digits2arr(digits, n);
    for (int i = n - 2; i >= 0; i -= 2) {
        digitArr[i] *= 2;
        if (digitArr[i] > 9)
            digitArr[i] -= 9;
    }
    
    int sum = 0;
    for (int j = 0; j < n; j++) {
        sum += digitArr[j];
    }
    if (sum % 10 == 0)
        return true;
    return false;
}

int getDigitCount(long digits) {
    int n = 0;
    while (digits) {
        digits /= 10;
        n++;
    }
    return n;
}

int *digits2arr(long digits, int length) {
    int *arr = malloc(length * sizeof(int));
    int i = length - 1;
    while (digits) {
        arr[i] = digits % 10;
        digits /= 10;
        i--;
    }
    return arr;
}
