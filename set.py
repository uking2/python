# Set is the collection of the unordered items.

# Each element in the set must be unique & immutable.

null_set = set( ) #empty set syntax
print("Empty set:", null_set)  # Output: Empty set: set()

nums = { 1, 2, 3, 4 }
print("Original set:", nums)  # Output: Original set: {1, 2, 3, 4}

set2 = { 1, 2, 2, 2 }
print("Set with duplicates removed:", set2)  # Output: Set with duplicates removed: {1, 2}

nums.add(5)
print("Set after adding 5:", nums)  # Output: Set after adding 5

nums.remove(2)
print("Set after removing 2:", nums)  # Output: Set after removing 2

# nums.clear()

# nums.pop()

# set = nums
# del nums  #deletes the set completely
# print(set)

# Set Operations
setA = { 1, 2, 3 }
setB = { 3, 4, 5 }

# Union
print("union",setA.union(setB))  # Output: {1, 2, 3, 4, 5}

# Intersection
print("intersection",setA.intersection(setB))  # Output: {3}
