import os
os.system("cls")
import random 
num = random.randint(0,11)
print(num)

for i in range(1,4)[::-1]:
    print(f"your chance balance {i}")
    innner = input("Guess a number between 1 and 10 :")
    try:
        innner = int(innner)
        os.system("cls")
        if( innner == num):
            print("\n................You guessed it...!\n")
            print("Thanks for playing . Bye :)")
            break
        
        else:
            if(num< innner):
                print("Too high ,try again")
            else:
                print("Too low ,try again")
        
    except:
        print("\n\t\tInvalid input")

print(f"Game over the number the is {num}")