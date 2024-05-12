a=int(input("Enter the First number :"))
b=int(input("Enter the Second number :"))
r=min(a,b)

while r:
    if a%r==0 and b%r==0:
        break
    r-=1

print(r)
