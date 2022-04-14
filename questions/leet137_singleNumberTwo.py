def leet137(arr: list):
    khali_set = set()
    sum1 = 0
    sum2 = 0
    for i in arr:
        sum1 = sum1 + i
        khali_set.add(i)
    for x in khali_set:
        sum2 = sum2 + (x*3)
    unique_num = int((sum2 - sum1)/2)
    print(unique_num)
    return unique_num


if __name__ == "__main__":
    given_arr = [9, 9, 9, 4, 5, 4, 4, 5, 5, 7]
    leet137(given_arr)
