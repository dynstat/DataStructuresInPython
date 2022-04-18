
def bubbleSort(arr):

    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


if __name__ == "__main__":
    arr = [45, 5, 3, 8, 9, 4]
    print(bubbleSort(arr))
