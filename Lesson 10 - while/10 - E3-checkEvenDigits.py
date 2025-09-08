
# qty of even number
# e.g. : 249 --> 2

number = int(input('Enter a number = '))
backup = number

count = 0

while backup != 0:
      digit = backup % 10

      if digit%2 == 0:
            count += 1
      
      backup = backup // 10

print(f'{number} has {count} even numbers')