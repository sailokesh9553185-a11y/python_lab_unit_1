# Demonstrate continue statement using for and while loops
print("For loop with continue (skip 5):")
for i in range(1, 8):
    if i == 5:
        continue
    print(i, end=" ")
print()

print("While loop with continue (skip 5):")
i = 0
while i < 7:
    i += 1
    if i == 5:
        continue
    print(i, end=" ")
print()
