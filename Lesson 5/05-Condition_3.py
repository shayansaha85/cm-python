
## NESTED IF

"""
Condition : 
Indian, age >= 18
"""

country = 'Pakistan'
age = 50

if country == 'India':
      if age >= 18:
            print('You are Indian and your age is >= 18')
      else:
            print('You are Indian but your age is not >=18')
else:
      print('Desh se bhaag tu!')
