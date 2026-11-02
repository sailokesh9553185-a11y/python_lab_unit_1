#python program to print the grade of a student using an elif ladder (Marks >= 90 → Grade A; >= 80 and < 90 → Grade B; >= 70 and < 80 → Grade C; < 70 → Grade D)

marks = int(input("Enter the number:"))
if marks >= 90:  
    print(f"Marks {marks}: Grade A")
elif marks >= 80:
    print(f"Marks {marks}: Grade B")
elif marks >= 70:  
    print(f"Marks {marks}: Grade C")
else:
    print(f"Marks {marks}: Grade D")
