# Right-angled triangle pattern
rows = int(input("Enter number of rows: "))
symbol = input("Enter symbol (e.g. * or 0): ")

for i in range(1, rows + 1):
    print((symbol + " ") * i)
