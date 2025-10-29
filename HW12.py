#Name: Diana Gonzalez
#Class: 5th Hour
#Assignment: HW12

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
import time
i = 5
while i >= 0:
    print (i)
    i -= 1
else:
    print ("Hello World!")
#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
d = 1
while d <= 30:
    if d % 2 == 0:
        print (d)
    d += 1

#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
e = 0
while e <= 30:
    if e % 3 == 0:
        e += 1
        continue
    else:
        print (e)
        e += 1
#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
import random
w = random.randint (1,6)
while w >= 6:
    print (w)
    if w == 1:
        break
    else:
        w = random.randint(1, 6)

#5. Create a while loop that asks for a number input until the user inputs the number 0.
p = int(input("press 0 to quit"))
while p != 0:
    p = int(input("press 0 to quit"))

