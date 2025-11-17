#Name:Diana
#Class: 5th Hour
#Assignment: SC3

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.

u = int(input("How many players are playing?"))
userRating = []
for number in range (u):
    p = int(input("Rate the model 1 to 5"))
    while p < 1 or p > 5:
        print ("The rating is out of range")
        p = int(input("Rating between 1 and 5:"))
    else:
        userRating.append(p)
sum = sum(userRating)
average = sum/u
print(average)





