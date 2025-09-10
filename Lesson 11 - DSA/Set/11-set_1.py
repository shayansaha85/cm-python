

# not subscriptable
# unique elements
# even if we provide duplicate elements, it will consider unique instances only

# s = { 43, 21, 88, 7, 92, 92, 88 }
# print(s)

li = [ 'India', 56, 72, 'Chandini', 'Chandini', 33 ]
si = set(li)

li_unique = list(si)

k = list(dict.fromkeys(li_unique))
print(k)