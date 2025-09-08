

country = input('Country : ')
age = int(input('Age : '))

if country == 'India': # Main IF block
      if age >= 18: # Nested IF block
            print('You are Indian and your age is >= 18')
      else: # Nested ELSE block
            print('You are Indian but your age is not >=18')
else: # Main ELSE block
      print('Desh se bhaag tu!')
