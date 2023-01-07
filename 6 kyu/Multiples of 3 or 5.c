int solution(int number) {
    if (number <= 2)
        return 0;
	int sum = 0;
    for (int i = number - 1; i > 2; i--) {
        if (i % 3 == 0 || i % 5 == 0)
            sum += i;
    }
    return sum;
}
