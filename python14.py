# list comprehension

list1 = ['alpha' , 'beta' , 'gamma' , 'delta' , 'tetra']
newlist = []

for i in list1:
    newlist.append(i)
print('Using For Loop :' ,newlist)

# instead we can write

newlist = [i for i in list1 if 'a' in i]
print('Using List Comprehension :',newlist)

# for other example

h_letters = [letter for letter in 'human']
print('Comprehension through String :' ,h_letters)

even = [number for number in range(21) if number % 2 == 0]
print(f'{even} is Even number')

odd = [number for number in range(21) if number % 2 != 0]
print(f'{even} is Odd number')


#Using function

def num(x):
    return x**2

number1 = [num(x) for x in range(21) if x % 2 == 0]
print('Using Function :',number1)


# Dictionary Comprehension...
string = 'Life is too short to argue , just ignore and move on'

dic = {d for d in string if d in 'aeiou'}
print('Using Dictionary comprehension :',dic)

# Using Key in Dictionary Comprehension...
square = {i : i ** 2 for i in range(11)}
print(' Using Key in Dictionary Comprehension',square)