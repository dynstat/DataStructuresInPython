# insertion sorting algorithm
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while key < arr[j] and j >= 0:

            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
    return arr


if __name__ == "__main__":
    arr = [4, 6, 1, 3, 9, 7, 5, 2]
    print(insertionSort(arr))
