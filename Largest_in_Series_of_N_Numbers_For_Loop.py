# Find the largest number in a series of N numbers using for loop
n = int(input("Enter how many numbers: "))
if n > 0:
    largest = float(input("Enter number 1: "))
    for i in range(1, n):
        num = float(input(f"Enter number {i+1}: "))
        if num > largest:
            largest = num
    print(f"The largest number is {largest}")
else:
    print("Invalid count.")
