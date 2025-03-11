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

def insertion_sort_optimized(arr: list = None) -> list:
    # Handle edge cases
    if arr is None or len(arr) <= 1:
        return arr
        
    for step in range(1, len(arr)):
        key = arr[step]
        # Use binary search to find the insertion position
        left, right = 0, step - 1
        
        # Binary search to find insertion position
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > key:
                right = mid - 1
            else:
                left = mid + 1
                
        # Shift elements to make room for the key
        for i in range(step - 1, left - 1, -1):
            arr[i + 1] = arr[i]
            
        arr[left] = key

    return arr

# driver code
if __name__ == "__main__":
    unsorted_array = [4, 6, 1, 3, 9, 7, 5, 2]
    print("Given unsorted Array: ", unsorted_array)
    # calling the insertion sort function
    sorted_array = insertion_sort(unsorted_array)
    print("Array after insertion sorting: ", sorted_array)
