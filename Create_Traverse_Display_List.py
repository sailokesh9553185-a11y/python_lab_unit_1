# Unit-3A_Task-1_Create_Traverse_Display_List.py
# Program to create, traverse and display elements of a list

# 1. Creating a list
my_list = [10, 20, 30, 40, 50, 60]
print("Created List:", my_list)

# 2. Traversing and displaying elements using a for-in loop
print("\n--- Traversing using a for-in loop ---")
for item in my_list:
    print(item, end=" ")
print()

# 3. Traversing and displaying elements using indices (range and len)
print("\n--- Traversing using indices ---")
for index in range(len(my_list)):
    print(f"Index {index}: {my_list[index]}")
