import random

num=random.randint(1,10)

i=int(input("Guess a number :"))
guess=1
while(num!=i):
    guess += 1
    if(i<num):
        print("No! it's lower than the target\n")
    else :
        print("No! it's higher than the target\n")

    i=int(input("Guess again :"))

    
print(f"You take {guess} time to guess correct answer")