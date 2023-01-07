def min_min_max(arr: list):
    arr.sort()
    minArr = arr[0]
    maxArr = arr[-1]
    absMin = None
    print(arr)
    for elem in arr:
        if not elem+1 in arr:
            absMin = elem + 1
            break;
    return [minArr, absMin, maxArr]
