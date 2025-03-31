# Program to sort a given array using bubble sort

def bubble_sort(arr: list) -> list:
    """
    Optimized bubble sort implementation that sorts a list in-place.
    
    Args:
        arr: List to be sorted
        
    Returns:
        Sorted list (same object as input)
    """
    if not arr or len(arr) <= 1:
        return arr
        
    arr_length = len(arr)
    # Track the last position where a swap occurred to reduce unnecessary comparisons
    last_swap_pos = arr_length - 1
    
    # Keep track of where the last swap happened in each pass
    while last_swap_pos > 0:
        new_last_swap_pos = 0
        for j in range(last_swap_pos):
            if arr[j] > arr[j+1]:  # change to "<" for descending order
                # swapping when a larger item is on its consecutive right
                arr[j], arr[j+1] = arr[j+1], arr[j]
                new_last_swap_pos = j
        
        # Update the boundary for the next iteration
        last_swap_pos = new_last_swap_pos
        
        # If no swaps occurred, the array is sorted
        if last_swap_pos == 0:
            break
            
    return arr


# driver code
if __name__ == "__main__":
    unsorted_array = [4, 6, 1, 3, 9, 7, 5, 2]
    print("Given unsorted Array: ", unsorted_array)
    # calling the bubble_sort function
    sorted_array = bubble_sort(unsorted_array)
    print("Array after bubble sorting: ", sorted_array)
