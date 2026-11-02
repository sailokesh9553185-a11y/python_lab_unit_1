# Demonstrate pass statement using for and while loops
print("For loop with pass:")
for i in range(1, 4):
    if i == 2:
        pass  # Placeholder
    print(f"Value: {i}")

print("While loop with pass:")
i = 1
while i <= 3:
    if i == 2:
        pass
    print(f"Value: {i}")
    i += 1
