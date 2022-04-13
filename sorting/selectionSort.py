#  program to sort the given array using selection sort

def selection_sort(arr: list):
    length = len(arr)
    for step in range(length):
        min_idx = step
        j = step + 1
        while (j < length):
            if arr[j] < arr[min_idx]:
                min_idx = j
            j += 1

        # swapping arr[step] and arr[min_idx]
        t = arr[step]
        arr[step] = arr[min_idx]
        arr[min_idx] = t

    return arr


# driver code
if __name__ == "__main__":
    unsorted_array = [4, 6, 1, 3, 9, 7, 5, 2]
    print("Given unsorted Array: ", unsorted_array)
    # calling the selection_sort function
    sorted_array = selection_sort(unsorted_array)
    print("Array after insertion sorting: ", sorted_array)
