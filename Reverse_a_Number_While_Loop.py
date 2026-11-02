# Reverse a given number using while loop
num = int(input("Enter an integer: "))
temp = abs(num)
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if num < 0:
    rev = -rev

print(f"Reversed number: {rev}")
