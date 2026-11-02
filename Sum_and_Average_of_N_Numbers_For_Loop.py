# Find sum and average of N numbers using for loop
n = int(input("Enter how many numbers: "))
total_sum = 0

for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    total_sum += num

average = total_sum / n if n > 0 else 0
print(f"Sum: {total_sum}, Average: {average}")
