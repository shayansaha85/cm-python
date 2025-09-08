
number = int(input('Enter a number = '))
backup1 = number
backup2 = number


count = 0

while backup1 != 0:
      backup1 = backup1 // 10
      count += 1

sum = 0

while backup2 != 0:
      rem = backup2 % 10
      sum += rem ** count
      backup2 = backup2 // 10

if number == sum:
      print('armstrong')
else:
      print('not armstrong')