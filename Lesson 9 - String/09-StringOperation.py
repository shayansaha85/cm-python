
# # string ==> vowels quantity

count = 0
name = input('Enter a string = ') # Shayan

for i in range(0, len(name)):
      if name[i].lower() == 'a' or name[i].lower() == 'e' or name[i].lower() == 'i' or name[i].lower() =='o' or name[i].lower() =='u':
            count = count+1

print(count)
