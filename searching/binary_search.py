# Given sorted array = [1,3,4,7,9,14,25,69,74,95,100,150]   consists of all the integers
#  Use binary search for finding any given element by returning its location or position in the array.


given_array = [1, 3, 4, 7, 9, 14, 25, 69, 74, 95, 100, 150]
to_find = 4


def binary_search(to_find, given_array):
    start = 0
    end = len(given_array)-1  # 12
    mid = 0
    # // rounds off the digit
    while (start <= end):
        mid = start + (end - start)//2
        # print("mid value ", given_array[mid])
        if to_find == given_array[mid]:
            return mid
        elif to_find < given_array[mid]:
            end = mid - 1
        elif to_find > given_array[mid]:
            start = mid+1


ans = binary_search(to_find, given_array)
if ans != None:
    print(
        f"The element {to_find} is found at position {ans}\n(Postion starts from Zero)")
else:
    print(f"{to_find} is not in this array")
