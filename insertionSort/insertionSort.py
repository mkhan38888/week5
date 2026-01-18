def insertion_sort_desc(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


numbers = [12, 11, 13, 5, 6]
print("Original list:", numbers)

insertion_sort_desc(numbers)
print("Sorted in decreasing order:", numbers)
