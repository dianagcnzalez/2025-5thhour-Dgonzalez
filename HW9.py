#Name: Diana Gonzalez
#Class: 6th Hour
#Assignment: HW9


#1. Print "Hello World!"
print ("Hello World!")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
import random
num1 = random.randint(1,10)
num2 = random.randint(1,10)
num3 = random.randint(1,10)
numList = [num1,num2,num3]
#3. Print the list.
print (numList)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if num1 >= num2 and num1 >= num3:
    print ("num 1 is the highest number")
elif num2 >= num1 and num2 >= num3:
    print ("num 2 is the highest number")
elif num3 >= num1 and num3 >= num2:
    print ("num 3 is the highest number")
#5. Tie the result (the largest number) from #4 to a variable called "num".
num = max(numList)
print (num)
#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 == 0:
    print ("num is divisible by 2")
elif num % 3 == 0:
    print ("num is divisible by 3")
elif num % 2 and num % 3 == 0:
    print ("num is divisible by both")
else:
    print ("num is divisible by neither")