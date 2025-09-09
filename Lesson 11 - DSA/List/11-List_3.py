
k = [53, 29, 72, 'Shayan']

print(k[2])
print(k[1:3])

k.insert(1, 'Chandini')
print(k)

# Nested indexing -- Coding MCQ
p = [ 45, 65, 33, [23, 74.2, 59, [ 'India', 'George', 99.24 ] ] ]

target = p[3][3][1]
print(target)


j = [ [54, '89', [ 99, 7, ['India', 'Shayan', 29], 26, ['b'] ]] ] 

target = j[0][2][2][1]
print(target)