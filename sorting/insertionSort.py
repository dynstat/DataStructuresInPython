# Program to sort a given array or list using insertion sort algorithm
def insertion_sort(arr: list = None):
    # Check if the input array is None or empty
    if arr is None or len(arr) == 0:
        return arr  # Return the array as is if it's None or empty

    # Iterate over the array starting from the second element
    for step in range(1, len(arr)):
        # Store the current value (key) to be positioned
        curr_val = arr[step]
        # Initialize the index of the last sorted element
        l_index = step - 1

        # Shift elements of the sorted segment to the right
        # until the correct position for curr_val is found
        while l_index >= 0 and curr_val < arr[l_index]:
            # Move the larger element one position to the right
            arr[l_index + 1] = arr[l_index]
            l_index -= 1  # Move to the left in the sorted segment

        # Place the current value at its correct position
        arr[l_index + 1] = curr_val

    return arr


def insertion_sort_optimized(arr: list = None) -> list:
    # Handle edge cases
    if arr is None or len(arr) <= 1:
        return arr

    for step in range(1, len(arr)):
        curr_val = arr[step]
        # Use binary search to find the insertion position
        left, right = 0, step - 1

        # Binary search to find insertion position
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > curr_val:
                right = mid - 1
            else:
                left = mid + 1

        # Shift elements to make room for the key
        for i in range(step - 1, left - 1, -1):
            arr[i + 1] = arr[i]

        arr[left] = curr_val

    return arr


# driver code
if __name__ == "__main__":
    unsorted_array = [4, 6, 1, 3, 9, 7, 5, 2]
    print("Given unsorted Array: ", unsorted_array)
    # calling the insertion sort function
    sorted_array = insertion_sort(unsorted_array)
    print("Array after insertion sorting: ", sorted_array)

    # calling the optimized insertion sort function
    sorted_array = insertion_sort_optimized(unsorted_array)
    print("Array after optimized insertion sorting: ", sorted_array)
