# Program to sort a given array using bubble sort

def bubble_sort(arr: list):
    arr_length = len(arr)
    # the "swap_occured" variable is to check if swapping occured or not (i.e. the given array is already sorted)
    # It will become True only when at least one swapping occured, this saves from unnecessary computation
    for i in range(arr_length):
        swap_occured = False
        for j in range(arr_length - i-1):
            if arr[j] > arr[j+1]:
                # swapping when a larger item is on its consecutive right
                (arr[j], arr[j+1]) = (arr[j+1], arr[j])
                swap_occured = True
        if not swap_occured:
            break

    return arr


# driver code
if __name__ == "__main__":
    unsorted_array = [4, 6, 1, 3, 9, 7, 5, 2]
    print("Given unsorted Array: ", unsorted_array)
    # calling the bubble_sort function
    sorted_array = bubble_sort(unsorted_array)
    print("Array after insertion sorting: ", sorted_array)
