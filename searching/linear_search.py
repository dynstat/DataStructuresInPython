#  program to search an item using linear search

def linear_search(arr: list, tofind):
    # return next((idx for idx,val in enumerate(arr) if val == tofind), None)
    for idx, val in enumerate(arr):
        if val == tofind:
            return idx
    return None


if __name__ == "__main__":
    array = [2, 4, 5, 6, 1, 7, 0, 3, 9]
    to_find = 10
    index = linear_search(array, to_find)
    if index is not None:
        print(f"The item {to_find} was found at index {index}", end="\n")
    else:
        print("Not found")
