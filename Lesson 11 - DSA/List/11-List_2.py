
l1 = [ 34,57,63 ]
print(l1)

lengthOfList = len(l1) # Finding length of the list
print(lengthOfList)

l1.append(23) # Adding element at last
print(l1)

l2 = l1.copy() # Old method of copying lists
print(l2)

l1.append(57)
print(l1)

countOf57 = l1.count(57) # Count of a specific element
print(countOf57)

l1.extend([6, 9]) # Adding more than 1 element
print(l1)

l1.remove(9) # Removing specific element
print(l1)

l1.pop() # Removing last element
print(l1)

