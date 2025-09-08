
name = 'ShAyAn'

print( name.upper() )
print( name.lower() )
print( len(name) )

# replace, count, find (first occurence)

greet_chandini = "Hello Chandini"
print(len(greet_chandini)) # 

greet_shayan = greet_chandini.replace( 'Chandini', 'Shayan' )
print(greet_shayan)

count_of_i = greet_chandini.count('i')
print(count_of_i)

index_of_C = greet_chandini.find('C')
print(index_of_C)

index_of_i = greet_chandini.find('i')
print(index_of_i)

first = "Hey"
second = "Shayan"

complete = first + " " + second # --> concatenation
print(complete)