# Check whether a string is a palindrome
s = input("Enter a string: ")
cleaned = "".join(s.lower().split())

if cleaned == cleaned[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
