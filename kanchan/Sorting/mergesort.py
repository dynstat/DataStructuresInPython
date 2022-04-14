# mergesort algorithm
def merge_sort(array):
    if len(array) > 1:

        # deviding the length of array
        mid = len(array)//2
        # deviding the array elements
        L = array[: mid]
        M = array[mid:]
        # sorting the first half
        merge_sort(L)
        # sorting the second half
        merge_sort(M)
        i = j = k = 0
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
        # if any element was left
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


if __name__ == "__main__":
    array = [12, 11, 13, 5, 6, 7]
    merge_sort(array)
