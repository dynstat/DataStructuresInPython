#  to find an element in the given array using binary search
def binarySearch(arr: list, to_find: int):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if to_find == arr[mid]:
            return mid
        if to_find < arr[mid]:
            high = mid-1
        if to_find > arr[mid]:
            low = mid+1


if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binarySearch(arr, to_find=7))
