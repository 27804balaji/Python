try:
    rangeloop=int(input("Enter the range :"))
    n=[]
    for i in range(1,rangeloop+1):
        num=int(input(f"Enter the {i} number :"))
        n.append(num)

    need_value=int(input("Enter the required number the list :"))

    if need_value in n:
        print("\nThe Position of the",need_value,"is :",n.index(need_value))

    elif need_value not in n:
        print('\n',need_value,"is not exist in the List!")

except ValueError:
    print("Enter a 'Number!'...")
