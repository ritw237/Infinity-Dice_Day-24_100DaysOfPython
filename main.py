print("INFINITY DICE 🎲!!!")

import random

number = int(input("Enter the number of sides you want on your dice: "))
roll_again = "yes"

def dice(num):
  
  roll = random.randint(1,num)
  print("You rolled: ",roll)
  
  
while roll_again=="yes":
    
    dice(number)    
    roll_again= input("roll again? ")
