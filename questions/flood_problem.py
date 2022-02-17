
# To find the total amount of water flooded between the buildings of different heights, due to rain.

# APPROACH
# create and fill the elements of two arrays that corresponds to the maximum tallest building on the left and right of the respective position (index) of the building_height array.

def min(x, y):
    if x < y:
        return x
    else:
        return y


def max(x, y):
    if x > y:
        return x
    else:
        return y


# sourcery skip: aug-assign
building_height = [2, 0, 4, 0, 2, 0, 1, 3]  # heights of different buildings
left_max_array = [0] * len(building_height)
right_max_array = []
temp = 0
for x in range(len(building_height)):
    left_max_array[x] = max(building_height[x], temp)
    temp = left_max_array[x]
temp = 0
for h in building_height[::-1]:
    right_max_array.append(max(h, temp))
    temp = max(h, temp)
right_max_array = right_max_array[::-1]
# print("right_max_array", right_max_array)
# print("left_max_array", left_max_array)

total_water = 0
array_len = len(building_height)
for pos in range(array_len):
    if building_height[pos] < left_max_array[pos] and building_height[pos] < right_max_array[pos]:
        water = min(left_max_array[pos],
                    right_max_array[pos]) - building_height[pos]
        total_water = total_water + water
print(total_water)
