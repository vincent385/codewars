int get_sum(int a, int b)
{
  int sum = 0;
  if (a < b) {
    for (int i = a; i < b + 1; i++) {
      sum += i;
    }
  }
  else {
    for (int i = b; i < a + 1; i++) {
      sum += i;
    }
  }
  return sum;
}
