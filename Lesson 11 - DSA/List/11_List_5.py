
num = [5, 6, 7, 31, 42]
# result = sum(num)
# print(result)

sum = 0

# generic for loop
for i in range(0, len(num)):
      if num[i]%2 == 0:
            sum = sum + num[i]

print(sum)


sum2 = 0
# For each loop
for n in num:
      if n%2 == 0:
            sum2 += n

print(sum2)