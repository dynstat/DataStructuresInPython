# Program to sort a given array or list using insertion sort algorithm
def insertion_sort(arr: list = None):
    for step in range(1, len(arr)):
        # key is the second item in the list
        curr_val = arr[step]
        # left denotes the index of the left item(s) of the key in every iteration in the loop...
        l_index = step-1
        # looping over all the items on the left of key as long as we find the number lesser than the key
        while l_index >= 0 and curr_val < arr[l_index]:
            # overwriting the larger items to their right indexes of the same array
            arr[l_index+1] = arr[l_index]
            l_index = l_index - 1
        arr[l_index+1] = curr_val  # placing the key at the desired index

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

