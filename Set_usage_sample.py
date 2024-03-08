## Sets do not allow duplicates
set_countries= {'col', 'mex', 'bol', 'ar'}
print(set_countries)
print(type(set_countries))

set_numbers = {1,4,5,6,7,8,9,9,9,9,9,9,9,9}
print(set_numbers)

set_types = {1, 'hi', False, 12.12}
print(set_numbers)

set_from_string = set('hello')
print(set_from_string)

set_from_tuple = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuple)

numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print (set_numbers)
#Reverting form a set to a list
unique_numbers = list(set_numbers)
print(unique_numbers)