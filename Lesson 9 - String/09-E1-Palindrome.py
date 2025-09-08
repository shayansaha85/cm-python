
name = input('Enter a string : ')
reverse = ""

lenOfName = len(name)

for i in range(lenOfName-1, -1, -1):
      reverse += name[i]

if name == reverse :
      print('Palindrome')
else:
      print('Not palindrome')