size=input("enter pizza size S/M/L")
bill=0
if size == 'S' or size=='s':
    bill +=100
    print("the amount is 100 RS")
elif size == 'M' or size=='m':
    bill +=200
    print("the amount is 200 RS")
else:
    bill +=300
    print("the amount is 300 RS")
pepperoni=input("do you want pepperoni y/N")
if pepperoni=='Y' or 'y':
    if size=='S' or 's':
        bill +=30
    else:
        bill +=50
extra_cheese=input("do you want extra cheese")
if extra_cheese=='y' or 'Y':
    bill +=20
    print(f"your final bill is {bill}")
