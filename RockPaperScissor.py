import random
user_choice=int(input("0 for rock,1 for paper and 2 for scissor"))
computer_choice=random.randint(0,2)
print("computer chose:",computer_choice)
if user_choice>=3 and user_choice<0:
    print("invalid input")
else:
    if computer_choice==user_choice:
        print("Its draw")
    elif computer_choice==0 and user_choice==2:
        print("you lose!")
    elif computer_choice==2 and user_choice==0:
        print("you win :)")
    elif computer_choice>user_choice:
        print("you lose!")
    elif user_choice>computer_choice:
        print("you win :)")

PIZZA ORDER IN PYTHON
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
