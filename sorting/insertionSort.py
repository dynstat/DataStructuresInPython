# Program to sort a given array or list using insertion sort algorithm
def insertion_sort(arr: list = None):
    for step in range(1, len(arr)):
        # key is the second item in the list
        key = arr[step]
        # left denotes the index of the left item(s) of the key in every iteration in the loop...
        left = step-1
        # looping over all the items on the left of key as long as we find the number lesser than the key
        while left >= 0 and key < arr[left]:
            # overwriting the larger items to their right indexes of the same array
            arr[left+1] = arr[left]
            left = left - 1
        arr[left+1] = key  # placing the key at the desired index

    return arr


# driver code
if __name__ == "__main__":
    unsorted_array = [4, 6, 1, 3, 9, 7, 5, 2]
    print("Given unsorted Array: ", unsorted_array)
    # calling the insertion sort function
    sorted_array = insertion_sort(unsorted_array)
    print("Array after insertion sorting: ", sorted_array)
