# Program to sort the given array using merge sort
def merge_sort(arr: list):
    if len(arr) <= 1:
        return

    start = 0
    end = len(arr) - 1
    mid = (end - start) // 2
    # splitting the arr into two parts
    left_arr = arr[start : mid + 1]
    # "end+1" because end position is not included in slicing
    right_arr = arr[mid + 1 : end + 1]

    merge_sort(left_arr)
    merge_sort(right_arr)

    i = j = k = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
    return arr


# driver code
if __name__ == "__main__":
    unsorted_array = [4, 6, 1, 3, 9, 7, 5, 2]
    print("Given unsorted Array: ", unsorted_array)
    # calling the merge sort function
    sorted_array = merge_sort(unsorted_array)  # merge sort array sorts in place
    print("Array after merge sort: ", unsorted_array, " ", sorted_array)
