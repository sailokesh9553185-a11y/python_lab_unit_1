# Demonstrate break statement using for and while loops
print("For loop with break (stop at 5):")
for i in range(1, 10):
    if i == 5:
        break
    print(i, end=" ")
print()

print("While loop with break (stop at 5):")
i = 1
while i < 10:
    if i == 5:
        break
    print(i, end=" ")
    i += 1
print()
