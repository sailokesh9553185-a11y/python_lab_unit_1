a=int(input("Enter the a"))
b=int(input("Enter the b"))
a , b = b , a
print(a,b)

a=a+b
b=a-b
a=a-b
print(a,b)
