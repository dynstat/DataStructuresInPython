def linear_search(arr, to_find):
    for i in range(len(arr)):
        if to_find == arr[i]:
            return i


# driver code
if __name__ == "__main__":
    array = [4, 6, 1, 3, 9, 7, 5, 2]
    print(linear_search(array, to_find=3))
