# Check whether a number is prime using for loop (1 to 100)
num = int(input("Enter a number between 1 and 100: "))
if num <= 1:
    print("Not prime")
else:
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    if flag:
        print("Prime number")
    else:
        print("Not a prime number")
