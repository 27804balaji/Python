class calculator:
    def __init__(self):
        self.choice = 0
        try:
            self.num_1=int(input("Enter a number :"))
            self.num_2=int(input("Enter a number :"))
            self.choice=int(input("Choose an Operator :"))
        except ValueError:
            print("Invalid Input")                          
                   
    def add(a,b):
        print(a+b)        

    def sub(a,b):
        print(a-b)        

    def mul(a,b):
        print(a*b)        

    def div(a,b):
        print(a/b)        
        
class condition(calculator):
    def cal(self):
        
        if self.choice == 1:
            print("\nResult :",end="")
            return calculator.add(self.num_1,self.num_2)
    
        elif self.choice == 2:
            print("\nResult :",end="")
            return calculator.sub(self.num_1,self.num_2)
    
        elif self.choice ==  3:
            print("\nResult :",end="")
            return calculator.mul(self.num_1,self.num_2)
             
        try:
            if self.choice == 4:
                print("\nResult :",end="")
                return calculator.div(self.num_1,self.num_2)
        except ZeroDivisionError:
            print("\nCan't Divide with Zero!...")
            
        else:
            print("\nEnter a valid Operator!")

        


class con(condition):
    def next_cal(self):
        nxt_cal = input("\nDo you want to Continue :('Yes'/'No') :")
       
        while nxt_cal == "NO" or nxt_cal == "no":
            break
            
        if nxt_cal == "YES" or nxt_cal == "yes":
            print("\n")
            calculator.__init__(self)
            condition.cal(self)
            self.next_cal()
            
            

obj = con()
obj.cal()
obj.next_cal()
print("\nThank You...\n")

