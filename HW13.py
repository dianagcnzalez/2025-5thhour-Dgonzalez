#Name: Diana Gonzalez
#Class: 5th Hour
#Assignment: HW13

#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".

#Create a while loop that follows the rules of the game.
m = 1
while m <= 100:
    if m % 3 == 0 and m % 5 == 0:
        print ("Fizzbuzz")
    elif m % 3 == 0:
            print ("Fizz")
    elif m % 5 == 0:
        print ("Buzz")
    else:
        print (m)
    m += 1





