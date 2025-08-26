#Name: Diana Gonzalez
#Class: 5th Hour
#Assignment: HW4


#1. Print Hello World!
print ("Hello World")
#1. Create a list with 5 strings containing 5 different names in it.
StringList =["Diana" , "Mardi" , "Casandra", "Kate" ,  "Emma"]
#2. Append a new name onto the Name List.
StringList.append("Korbyn")
#3. Print out the 4th name on the list.
print (StringList[3])
#4. Create a list with 4 different integers in it.
intList = [ 0,2,1,4]
#5. Insert a new integer into the 2nd spot and print the new list.
intList.insert(1,5)
print (intList)
#6. Sort the list from lowest to highest and print the sorted list.
intList.sort()
print (intList.sort)
#7. Add the 1st three numbers on the sorted list together and print the sum.
intList_sum = intList[0] + intList[1] + intList[2]
print (intList_sum)
#8. Create a list with two strings, two variables, and too boolean values.
mixList = ["one", "cow", 5, 7, False, True]
print (mixList)
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(mixList[int(input(6))])