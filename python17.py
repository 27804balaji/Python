# filter() function

from functools import reduce


list_1 = list(range(-10 , 10))
# print(list_1)
list_2 = []

for i in list_1:
    if i < 0:
        list_2.append(i)
print('Using for loop :',list_2)

#Instead of above code...
print('Using filter :',list(filter((lambda x :  x < 0) ,  list_1)))

# reduce() function

num = [1 , 2 , 3 , 4 , 5]
li = 0

for i in num:
    li += i
print("Using for loop :",li)

# Instead of above code...

def sum(a , b):
    return a + b

print('Using reduce() function :' , reduce(sum , num))
