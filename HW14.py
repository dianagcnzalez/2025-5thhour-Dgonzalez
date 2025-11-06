#Name: Diana Gonzalez
#Class: 5th Hour
#Assignment: HW14
import time

#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.
for i in range (5,0,-1):
    print (i)
else:
    print ("Hello World!")
#2. Create a for loop that counts up and prints only even numbers between 1 and 30.
for a in range (1, 31,+1):
    if a % 2 == 0:
        print (a)
#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.
for b in range (1, 31,2):
    if b % 3 == 0:
        continue
    else:
        print (b)
#4. Create a for loop that prints 5 different animals from a list.
animals = [ "cat", "dog", "goat", "cow", "mouse"]
for animals in animals:
    print (animals)
#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
for d in input("Reverse a string: ")[::-1]:
    print (d)
#6. Create a list containing 10 integers of your choice and print the list.
numList = [1,2,3,4,5,6,7,8,9,10]
print (numList)
#7. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers = 0
oddNumbers = 0
#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.
for e in numList:
    if e % 2 == 0:
        evenNumbers += 1
    else:
        oddNumbers += 1
print (evenNumbers, oddNumbers)

#9. Create a variable that asks the user for an integer and an empty integer variable.
var = int(input("Enter a number: "))
x= 1
#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)
for m in range (1 ,var + 1):
    x*=m
print (x)


