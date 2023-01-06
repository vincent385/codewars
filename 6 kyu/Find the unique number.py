def find_uniq(arr):
    mapped = {}
    for elem in arr:
        if mapped.get(elem):
            mapped[elem] += 1
        else:
            mapped[elem] = 1
    for k, v in mapped.items():
        if v == 1:
            return k
