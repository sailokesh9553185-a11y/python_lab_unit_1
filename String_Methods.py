# Demonstrate common string methods
s = "  Python Programming Language  "
print("Original:", repr(s))
print("Upper:", s.upper())
print("Lower:", s.lower())
print("Strip:", repr(s.strip()))
print("Split:", s.split())

words = ["Hello", "World"]
print("Join:", " ".join(words))
print("Replace:", s.replace("Python", "Java"))
print("Find 'Program':", s.find("Program"))
