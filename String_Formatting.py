# Demonstrate string formatting (format(), f-strings, % operator)
name = "Alice"
age = 25

# 1. f-string
print(f"Name: {name}, Age: {age}")

# 2. format() method
print("Name: {}, Age: {}".format(name, age))

# 3. % operator
print("Name: %s, Age: %d" % (name, age))
