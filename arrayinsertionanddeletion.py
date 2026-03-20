#Name: Katlyne Kaziga
#Reg number: AIIM/01432/2024

#Insertion and Deletion of Arrays

#Creating an array
arr = [5, 10, 15, 20, 25]
print("Original array:", arr)

#Insertion of an array
i = int(input("Insert position: "))
v = int(input("Value: "))
arr.insert(i,v)
print("After insert:", arr)

# Deletion 
d = int(input("Delete position: "))
arr.pop(d)
print("After delete:", arr)
