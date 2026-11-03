# Unit-3A_Task-4_Remove_Duplicates_from_List.py
# Program to remove duplicate elements from a list

my_list = [10, 20, 10, 30, 40, 20, 50, 30]
print("Original List with duplicates:", my_list)

# Method 1: Using dict.fromkeys() to remove duplicates while preserving original order
unique_list = list(dict.fromkeys(my_list))
print("List after removing duplicates (preserving order):", unique_list)

# Method 2: Using a simple loop
# unique_list = []
# for item in my_list:
#     if item not in unique_list:
#         unique_list.append(item)
# print("List using loop:", unique_list)
