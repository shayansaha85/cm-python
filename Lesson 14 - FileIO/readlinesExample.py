
file = open('numbers.txt', 'r')
data = file.readlines()
file.close()

sum = 0

for x in data:
      v = x.strip()
      v_int = int(v)
      sum += v_int

countofnumbers = len(data)
average = sum / countofnumbers

print(average)