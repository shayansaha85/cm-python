
name = input('Enter a string = ') # c h a n d i n i
reverse = ""

k = len(name) - 1 # 7

while k >= 0:
      reverse = reverse + name[k] # inidnahc
      k = k-1 # -1

if reverse == name:
      print('palindrome')
else:
      print('not palindrome')