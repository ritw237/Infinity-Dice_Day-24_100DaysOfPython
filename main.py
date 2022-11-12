print("INFINITY DICE 🎲!!!")

import random

def dice(num):
  roll_again = input("Do you want to roll?: ")
  while roll_again=="yes":
    roll = random.randint(1,num)
    print("You rolled: ",roll)
    dice(num)
    
    
number = int(input("Enter the number of sides you want on your dice: "))



dice(number)