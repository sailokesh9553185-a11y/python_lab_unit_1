# Print multiplication table using for and while loops
num = int(input("Enter a number: "))

print(f"Multiplication Table for {num} (using for loop):")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print(f"\nMultiplication Table for {num} (using while loop):")
i = 1
while i <= 11:
    print(f"{num} x {i} = {num * i}")
    i += 1
