def max_distinct_naive(arr):
    n = len(arr)
    max_len = 0

    for i in range(n):
        for j in range(i, n):
            seen = set()
            valid = True
            for k in range(i, j + 1):
                if arr[k] in seen:
                    valid = False
                    break
                seen.add(arr[k])
            if valid:
                max_len = max(max_len, j - i + 1)

    return max_len


def main():
    arr = list(map(int, input("Enter array elements separated by space: ").split()))
    result = max_distinct_naive(arr)
    print("Maximum length of distinct segment (Naive):", result)



main()
