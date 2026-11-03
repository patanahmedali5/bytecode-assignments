first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
third = float(input("Enter the third number: "))

if first >= second:
    if first >= third:
        largest = first
    else:
        largest = third
else:
    if second >= third:
        largest = second
    else:
        largest = third

print("Largest number:", largest)
