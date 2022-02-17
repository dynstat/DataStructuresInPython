d1 = {'a': 1, 'b': 3, 'c': 5, 'd': 4}

# print(d1['c'])
# print(d1.keys())

for i in d1:
    y = 4
    # print(d1[i])
    if d1[i] == 'hello':
        d1[i] = "good"

d1['newKey'] = 5

# print(d1['a'])
x = list(d1.values())
x = sorted(x)
print(x)


def keyFinder(x):
    for items in d1:
        if
