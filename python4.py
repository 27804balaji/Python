num=int(input("Enter the Number to 'Prime' (or) 'Not' :" ))
r=num/2
flag=True
for i in range(2,int(r)+1):
    if num%i==0:
        flag=False
        break

if flag:
    print(num,"is Prime...")
else:
    print(num,"is not Prime...")
    
