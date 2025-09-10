#Name: Diana Gonzalez
#Class: 5th Hour
#Assignment: playground

#We're going to make a simple game that asks you to guess a number 1-2000.

import random
numList = random.randint(1,2000)
print (numList)
#Now pick a number you want.
number_You_guess = int(input("Guess a number between 1 and 2000?"))
print ("Now add 345 to the random number")
New_num = numList + 345
print (New_num)
number = input("Is your number odd or even?")
print ("if you got an odd number you win! ")
