def max_distinct_optimized(arr):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(arr)):
        while arr[right] in seen:
            seen.remove(arr[left])
            left += 1
        seen.add(arr[right])
        max_len = max(max_len, right - left + 1)

    return max_len


def main():
    arr = list(map(int, input("Enter array elements separated by space: ").split()))
    result = max_distinct_optimized(arr)
    print("Maximum length of distinct segment (Optimized):", result)



main()
