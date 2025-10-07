#Name: Diana Gonzalez
#Class: 6th Hour
#Assignment: HW9


#1. Print "Hello World!"
print ("Hello World!")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
import random
numList= [random.randint(1,100), random.randint(1,100), random.randint(1,100)]
#3 . Print the list.
print (numList)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if numList[0] >= numList[1] and numList[0] >= numList[2]:
    print (f"{numList[0]} is the largest")
    num = numList[0]
elif numList[1] >= numList[0] and numList[1] >= numList[2]:
    print (f"{numList[1]} is the largest")
    num = numList[1]
elif numList[2] >= numList[0] and numList[2] >= numList[1]:
    print (f"{numList[2]} is the largest")
    num = numList[2]
#5. Tie the result (the largest number) from #4 to a variable called "num".
num = max(numList)
print (num)
#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 == 0:
    if num % 3 == 0:
        print("Is both divisible by 2 and 3")
    else:
        print("Is divisible by 2 but not 3")
else:
    if num % 3 == 0:
        print("Is both divisible by 3 but not 2")
    else:
        print("Is divisible by neither")