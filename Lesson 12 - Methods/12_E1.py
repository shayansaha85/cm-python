##### Saree Dukan : Products
##### > 999 --> all prime digits --> sum --> sum%

def isPrime(number):
      if number in [0,1]:
            return False
      else:
            count = 0
            for i in range(2,number+1):
                  if number%i == 0:
                        count += 1
            if count == 1:
                  return True
            else:
                  return False
            

try:
      price = int(input('Enter the price : '))

      primeDigits = []
      totalPrime = 0

      if price <= 999:
            print('Gareeb aurat!!')
      else:
            print('Wah! Tu toh ameer hai!!')

            backup = price # 3979
            while backup!=0: # True, True, True, True, False
                  rem = backup % 10 # 9,7,9,3
                  if isPrime(rem): # False, True, False, True
                        primeDigits.append(rem) # [7, 3]
                  backup = backup // 10 # 397, 39, 3, 0
            
            for pd in primeDigits:
                  totalPrime = totalPrime + pd # 7, 10
            
            discountedPrice = price - price * (totalPrime/100)
            discountedPrice_final = round(discountedPrice, 2)

            print(f'Aap {discountedPrice_final} price dijiye, aur dukan se dafa ho jaiyen!')
except:
      print('Sahi se bata faltu aurat!!')