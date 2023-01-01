#include <bits/stdc++.h>
using namespace std;

int square_digits(int num) {
	size_t arrsz = log10(num) + 1;
	int arr[arrsz];
	int i = 0;
	while (num) {
		arr[i++] = num % 10;
		num /= 10;
	}

	unsigned sq;
	num = 0;
	for (int i = arrsz - 1; i >= 0; i--) {
		sq = arr[i] * arr[i];
		if (sq / 10) {
			num = num * 10 + sq / 10;
			num = num * 10 + sq % 10;
		} else {
			num = num * 10 + sq;
		}
	}

	return num;
}
