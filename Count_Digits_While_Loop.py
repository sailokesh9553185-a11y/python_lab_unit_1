# Count the number of digits in a number using while loop
num = int(input("Enter an integer: "))
temp = abs(num)
count = 0

if temp == 0:
    count = 1
else:
    while temp > 0:
        count += 1
        temp //= 10

print(f"Number of digits: {count}")
