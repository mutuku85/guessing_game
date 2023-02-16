#this program demonstrates a guessing game
from random import randint 

#1.get user input
user_name=input("What's your name?")
print("Hello there"+user_name+"!")
number=randint(10,50)

#2.using a while loop
counter=0 
while counter<5:
    user_number=eval(input("enter number"))
    counter+=1
    if user_number<number:
     print("Your guess is too low")
    elif user_number>number:
     print("Your number is too high")
    elif user_number==number:
     print("You win")
     break
print("Game over.")
if user_number==number:
    print("You win")
else:
    print("The correct number was")
    print(number)
