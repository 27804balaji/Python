#Decorator...
import numpy

def fun(x):
    return x+1
fun(10)

then = fun
print(then(20))

# Function inside function(nested function)

def first():
    def second():
        print('Hi! I am Second function')
        print('Im good now')

    print('Hi! I am First Funcion')
    print('Im good')
    second()

first()


list1 = [1 , 2 , 3 , 4 , 5]
list2 = []

for x  in list1:
    list2.append(x ** 2)

print('Using append function :',list2)

def square(x):
    return x ** 2

# Using map() function
print('Using map function :',list(map(square , list1)))

# Using lambda with map()function
print('Using Lambda function :' ,list(map((lambda x : x ** 2) , list1)))


def sqre(x):
    return x ** 2

def cube(x):
    return x ** 3

def sqrt(x):
    return numpy.sqrt(x)

functions = [sqre , cube , sqrt]

for i in range(5):
    values = (list(map((lambda x : x(i)) , functions)))
    print(values)

# Using multiple argument
list_variable = [1 , 3 , 5 , 7 , 9]
tuple_variable = (2 , 4 , 6 , 8 , 10)

print(list(map((lambda x , y : y * x ) ,  list_variable , tuple_variable)))


