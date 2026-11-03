# File: Unit-3B_Task-2_Tuple_Operations.py

print("--- 1. Tuple Concatenation ---")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(f"Tuple 1: {tuple1}")
print(f"Tuple 2: {tuple2}")
print("Concatenated Tuple:", concatenated_tuple)

print("\n--- 2. Tuple Slicing ---")
numbers = (10, 20, 30, 40, 50, 60, 70, 80)
print("Original Tuple:", numbers)
print("Elements from index 2 to 5:", numbers[2:6])
print("Elements from beginning up to index 4:", numbers[:5])
print("Elements from index 3 to end:", numbers[3:])
print("Every second element (step 2):", numbers[::2])

print("\n--- 3. Tuple Unpacking ---")
person = ("Alice", 28, "Data Scientist")
name, age, profession = person
print("Unpacked values:")
print("Name:", name)
print("Age:", age)
print("Profession:", profession)
