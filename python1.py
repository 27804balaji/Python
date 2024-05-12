try:
    days=int(input("Enter the number of Days : "))
    hours=days*24
    minutes=hours*60
    seconds=minutes*60
    milliseconds=seconds*60
    print(days,"days has",hours,"hours",minutes,"minutes",seconds,"seconds",milliseconds,"milliseconds...")    
            
except ValueError:
        print("Isn't a Valid number ,Give Valid number...")
