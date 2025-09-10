
number = int(input('Enter a number = ')) # 7
count = 0

if number in [1,0]:
      print('NON-PRIME')
else:
      for i in range(2, number):
            if number%i == 0:
                  count += 1
                  break
      if count == 0:
            print('PRIME')
      else:
            print('NON PRIME')
