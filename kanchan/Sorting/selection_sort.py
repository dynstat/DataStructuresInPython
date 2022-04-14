# selection sorting algorthm

def selectionSort(arr: list):
    length = len(arr)
    for i in range(length):
        id_min = i
        j = i+1
        while(j < length):
            if arr[j] < arr[id_min]:
                id_min = j
            j = j+1
        temp = arr[i]
        arr[i] = arr[id_min]
        arr[id_min] = temp
    return arr


if __name__ == "__main__":
    print("before sorting")
    arr = [6, 3, 2, 4, 1, 0]
    print(arr)
    print("after sorting")
    print(selectionSort(arr))
