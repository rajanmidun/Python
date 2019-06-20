print("Enter 3 numbers to check greatest number")
first=int(input("First Number: "))
second=int(input("Second Number: "))
third=int(input("Third Number: "))

if(first>second and first>third):
    print(f"{first} is greater than {second} and {third}")

elif(second>first and second>third):
    print(f"{second} is greater than {first} and {third}")

else:
    print(f"{third} is greater than {first} and {second}")