import random
import string
choice= input("do you want to roll a dice (y/n)?").lower()
if choice== 'y':
    die1=random.randint (1,6)
    die2=random.randint (1,6)
    print(f"({die1},{die2})")
elif choice=='n':
    print("Thank you:)")
    exit()
else:
    print("Invalid choice!")
