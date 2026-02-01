from typing import List

def mergesort(arr: List[int]) -> List[int]:
    """
    Merge Sort (not in-place, stable).
    Time: O(n log n) worst/avg/best
    Space: O(n)
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    # merge step
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Example:
# data = [5, 2, 9, 1, 5, 6]
# print(mergesort(data))


def main():
    print("merge sort")
    print(mergesort([1, 3, 3, 4, 2, 6, 9, 8, 7]))
if __name__ == "__main__":
    main()