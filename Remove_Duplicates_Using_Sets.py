# Unit-3C_Task-3_Remove_Duplicates_Using_Sets.py

# Original list containing duplicate values
original_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]
print("Original List:", original_list)

# Remove duplicates by converting the list to a set
unique_set = set(original_list)
print("Converted to Set (Duplicates Removed):", unique_set)

# Convert the set back to a list (if list format is needed)
unique_list = list(unique_set)
print("Converted back to List:", unique_list)
