int maxMultiple(int divisor, int bound) 
{
    int n;
    for (int i = 0; i < bound + 1; i++) {
        if (i % divisor == 0) {
            n = i;
        }
    }
    return n;
}
