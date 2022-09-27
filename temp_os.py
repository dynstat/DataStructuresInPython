import os

# c = 0
# for ch in __file__[::-1]:
#     if ch != "\\":
#         c +=1
#         continue
#     break
# curr_fold = __file__[:-(c):]
curr_folder = os.path.dirname(__file__)
# print(__file__)
# print(curr_folder)
file_name = os.path.basename(r"D:\Python_Folder\data_structures\searching\linear.search.py")
print(file_name)
for (path, folders_list, files_list) in os.walk(r"D:\Python_Folder\django_prac\django_api_pract\api_test"):
    for file in files_list:
        if file.endswith("py"):
            print(f"{file}") 
    break





