n=int(input("Enter the Limit :"))
nums=[]
for i in range(1,n+1):
    number=int(input(f"Enter the {i} number :"))
    nums.append(number)
print("Enter the needed value's index :",end="")
m=int(input())
print("Result :",nums[m],end="")