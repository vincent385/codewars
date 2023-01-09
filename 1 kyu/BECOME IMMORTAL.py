def elderAge(m, n, l, t):
    ssum = 0
    for i in range(n):
        for j in range(m):
            ssum += (i^j) - l if (i^j) - l >= 0 else 0
    return ssum if ssum < t else ssum - t


if __name__ == '__main__':
    print(elderAge(8, 5, 1, 100))
