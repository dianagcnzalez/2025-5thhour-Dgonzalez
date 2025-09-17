#Name:Diana Gonzalez
#Class: 5th Hour
#Assignment: HW7

#1. Print Hello World!
print ("Hello World")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
dianasDict = {
  "name": "diana",
  "age" : "seventeen",
  "birthdate": [2,14,2008]
}
#3. Print the keys of the dictionary from #2.
print (dianasDict.keys())
#4. Print the values of the dictionary from #2
print (dianasDict.values())
#5. Print one of the three numbers from the list by itself
print (dianasDict["birthdate"][1])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
dianasDict.update ({"height": 5 })
#7. Print the entire dictionary from #2 with the updated key and value.
print (dianasDict)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
studentsDict = {
    "classmate 1": {
        "name": "mardi",
        "age":"mardi",
        "height":"five six"
    },
    "classmate 2":{
        "name":"Waylon",
        "age": "seventeen",
        "height": "five seven",
    },
    "classmate 3": {
        "name":"Hogan",
        "age": "fifteen",
        "height": "five five",
    },
}
#9. Print the names of all three classmates on the same line.
print (studentsDict.keys())
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
studentsDict.pop("classmate 3")
print (studentsDict)