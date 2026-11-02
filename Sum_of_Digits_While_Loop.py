# Find sum of digits of a number using while loop
num = int(input("Enter an integer: "))
temp = abs(num)
total_sum = 0

while temp > 0:
    digit = temp % 10
    total_sum += digit
    temp //= 10

print(f"Sum of digits of {num} is {total_sum}")
