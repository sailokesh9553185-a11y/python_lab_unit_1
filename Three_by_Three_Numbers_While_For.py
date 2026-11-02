# Print numbers in a 3x3 grid using while-for nested loop
num = 1
i = 0
while i < 3:
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()
    i += 1
