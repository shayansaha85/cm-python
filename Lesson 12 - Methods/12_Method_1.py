
number = [73, 52, 39, 25, 63]

def even_checker(n): # 1 argument function/method
      if n%2 == 0:
            return True
      else:
            return False


for i in number:
      if even_checker(i):
            print(f'{i} is even')
      else:
            print(f'{i} is odd')