# tuple is an immutable sequence type in Python, meaning its elements cannot be changed after creation.

tuple =(1,2,3,4,5)
print("Original tuple:", tuple)
  # Output: Original tuple: (1, 2, 3, 4, 5)

new_list = list(tuple)
  

new_list.append(6)
print("List after appending 6:", new_list)  # Output: List after appending 6: [1, 2, 3, 4, 5, 6]

tuple1 =(1,2,3,4,2)

tuple1.count(2)
print("Count of 2 in tuple1:", tuple1.count(2))  # Output

tuple1.index(4)
print("Index of 4 in tuple1:", tuple1.index(4))  # Output

print(tuple1[1:4])

