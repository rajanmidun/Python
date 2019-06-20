#multiplication table of any number
number=int(input("Enter number "))

for i in range(10):
    print(f"{number}*{i+1} ={number*(i+1)}")