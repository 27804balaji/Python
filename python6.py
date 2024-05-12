from datetime import datetime

dob=input("Enter your Birthday Date :")
dob_1=datetime.strptime(dob,"%d/%m/%Y")
print(dob_1)
print("Today's Date :",datetime.today())
print("\n",datetime.today()-dob_1,"days you lived in this World!...")
