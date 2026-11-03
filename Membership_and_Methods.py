# Unit-3C_Task-2_Set_Membership_and_Methods.py

# Initial set
my_set = {10, 20, 30, 40}
print("Initial Set:", my_set)

# 1. Membership Testing (in / not in)
print("\n--- Membership Testing ---")
print("Is 20 in my_set?", 20 in my_set)
print("Is 50 not in my_set?", 50 not in my_set)

# 2. Add Method
print("\n--- Add Method ---")
my_set.add(50)
print("After adding 50:", my_set)

# 3. Remove Method (Raises a KeyError if the element is not found)
print("\n--- Remove Method ---")
my_set.remove(20)
print("After removing 20:", my_set)

# 4. Discard Method (Does NOT raise an error if the element is missing)
print("\n--- Discard Method ---")
my_set.discard(30)
print("After discarding 30:", my_set)

# Discarding a non-existent element safely ignores it without crashing
my_set.discard(100)
print("After discarding non-existent 100:", my_set)
