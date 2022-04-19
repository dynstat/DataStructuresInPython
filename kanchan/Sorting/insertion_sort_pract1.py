# program to sort the given array using insertion sort

def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        key = arr[i]
        for j in range(i-1, -1, -1):
            if key < arr[j] and j > 0:
                # shifting by overwriting consecutive right index value
                arr[j+1] = arr[j]
            elif j == 0 and key < arr[j]:
                arr[j+1] = arr[j]  # shifting by overwriting
                arr[j] = key    # putting the key in index 0 as j=0 in this case

            else:
                arr[j+1] = key  # putting the key in the desired position
                break
    return arr


if __name__ == "__main__":
    unsorted_array = [6, 3, 5, 4, 2]
    sorted_array = i(unsorted_array)
    print(f"array after sorting is: {sorted_array}")
