#list in python

name=["Rajan","Raghbendra","Bibhu","Firoj","Rajan"]
print(name)

#insert at last
print("After inserting data")
name.append("Pasang")
print(name)

#insert at specific point
print("Inserting at specific point")
name.insert(2,"Kaka")
print(name)

#remove specific element
print("Remove an item")
name.remove("Rajan")
print(name)

#remove last element
print("Remove last element")
name.pop()
print(name)

#sorting the element
print("Sorting name")
name.sort()
print(name)


print(name[2:])
name[0]="Raghu"

#change the value
print(name)