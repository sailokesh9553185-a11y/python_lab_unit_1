# Check whether a number is a palindrome using while loop
num = int(input("Enter an integer: "))
temp = abs(num)
rev = 0

while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10

if abs(num) == rev:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
