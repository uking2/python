list = [2,1,3]
print("Original list:", list)  # Output: Original list: [2, 1, 3]

list.append(4)
print("List after append:", list)  # Output: List after append: [2, 1, 3, 4]

list.sort()
print("Sorted list:", list)  # Output: Sorted list: [1, 2, 3, 4]

list.sort(reverse=True)
print("List sorted in descending order:", list)  # Output: List sorted in descending order: [4, 3, 2, 1]

list.reverse()
print("Reversed list:", list)  # Output: Reversed list: [1, 2, 3, 4]

list.remove(3)#if here we have duplicate value it will remove first occurence
print("List after removing 3:", list)  # Output: List after removing 3

list.insert(1, 5)
print("List after inserting 5 at index 1:", list)  # Output: List

list.pop(1)# pop removes last element
print("List after popping element at index 1:", list)  # Output: List