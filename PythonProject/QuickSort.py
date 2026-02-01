from typing import List

def quicksort_inplace(arr: List[int]) -> List[int]:

    def partition(low: int, high: int) -> int:
        pivot = arr[high]   # choose last element as pivot
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        # place pivot in correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def qs(low: int, high: int) -> None:
        if low < high:
            p = partition(low, high)
            qs(low, p - 1)
            qs(p + 1, high)

    qs(0, len(arr) - 1)
    return arr


def main():
    print("quick sort")
    print(quicksort_inplace([1, 3, 3, 4, 2, 6, 9, 8, 7]))
if __name__ == "__main__":
    main()