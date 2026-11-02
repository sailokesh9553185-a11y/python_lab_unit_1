# Print numbers in a 3x3 grid using for-for nested loop
num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()
