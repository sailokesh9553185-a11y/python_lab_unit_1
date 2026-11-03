# Unit-3C_Task-1_Set_Creation_Basic_Operations.py

# 1. Set Creation
# Using curly braces
set_a = {1, 2, 3, 4, 5}
# Using the set() constructor from a list
set_b = set([4, 5, 6, 7, 8])

print("Set A:", set_a)
print("Set B:", set_b)

# 2. Union Operation (Elements in A, B, or both)
union_result = set_a.union(set_b)  # Can also use: set_a | set_b
print("\nUnion (A | B):", union_result)

# 3. Intersection Operation (Elements common to both A and B)
intersection_result = set_a.intersection(set_b)  # Can also use: set_a & set_b
print("Intersection (A & B):", intersection_result)

# 4. Difference Operation (Elements in A that are not in B)
difference_result = set_a.difference(set_b)  # Can also use: set_a - set_b
print("Difference (A - B):", difference_result)
