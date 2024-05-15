# Introduction to Genrators...

def fun():
    n = 1
    print('The First Executon')

    yield n
    n += 1
    print('The Second Execution')

    yield n
    n += 1
    print('The Last Execution')

    yield n

my = fun()
print(next(my))
print(next(my))
print(next(my))

# Instead of the above commented code we can use iteraration...

for i in fun():
    print(i)


# Other Example

list_1 = [2 , 4 , 6 , 8 , 10]
generator = (x ** 2 for x in list_1)
print('The Generator Object :',generator) #It prints the object of the generator.
#Instead use iterator.

for index in generator:
    print(index)


# Pypline using Genertors...

def fibanonic(num):
    x , y = 0 ,1
    for i in range(num):
        x , y = y , x+y
        yield x

def square(num):
    for ind in num:
        yield ind ** 2

print(sum(square(fibanonic(10))))

#Other way using Generator...

def funt(limit):
    a = 0
    b = 1

    while a < limit:
        yield a
        a , b = b , a+b
x = funt(5)
print('Fibanoic Series ')
print(next(x))
print(next(x))
print(next(x))
print(next(x))

print('\nUsing Iterator :')

for j in funt(5):
    print(j)


# Handle the StopIteration...

value = 'Balaji'
iter_value = iter(value)
print('\n')

while True:
    try:
        item = next(iter_value)
        print(item)
    except StopIteration:
        break

#Using Class...
print('\n')
class gen:
    def __init__(self , max = 0):
        
        self.max = max
        
    
    def __iter__(self):
        self.n = 0
        return self
        

    def __next__(self):
        if self.n < self.max:
            result = self.n+6
            self.n  += 1
            return result
        
        else:
            raise StopIteration
        
ok = gen(9)
k = iter(ok)

for bal in k:
    print(bal)