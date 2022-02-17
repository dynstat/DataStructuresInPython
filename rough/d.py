# vxl_org = [[1], [3]]
# vxl_org[1].append([1])
# vxl_org[1][1].append(2)
# print(vxl_org)
# vx_list = [0, 1, 2, 3, 4]

# for v in vx_list:
#     vxl = list((v,))
#     if vxl in vxl_org:
#         print("found", vxl)


#############################################################
# converting dictionary to list
graph_elements = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"]
}
gl = [(k, v) for k, v in graph_elements.items()]
print(gl)
# Output --->    [('a', ['b', 'c']), ('b', ['a', 'd']), ('c', ['a', 'd']), ('d', ['e']), ('e', ['d'])]
#############################################################
