#Name:Diana Gonzalez
#Class: 5th Hour
#Assignment: HW5


#1. Create a list with 9 different numbers inside.
intList = [0,1,2,3,4,5,6,7,8]
#2. Sort the list from highest to lowest.
intList.sort(reverse=True)
print(intList)
#3. Create an empty list.
secondList = []
#4. Remove the median number from the first list and add it to the second list.
numberFour = intList[4]
intList.pop(4)
secondList.append(numberFour)
#5. Remove the first number from the first list and add it to the second list.
numberZero = intList [0]
intList.pop(0)
secondList.append(numberZero)
#6. Print both lists.
print (intList)
print (secondList)
#7. Add the two numbers in the second list together and print the result.
intSumList = (secondList[0] + secondList[1])
print (intSumList)
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
secondList.pop(1)
secondList.pop(0)
intList.append(intSumList)
#9. Sort the first list from lowest to highest and print it.
intList.sort()
print (intList)