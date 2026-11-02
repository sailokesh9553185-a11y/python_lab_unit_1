# Print an NxN grid of stars based on user input
n = int(input("Enter grid size: "))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
