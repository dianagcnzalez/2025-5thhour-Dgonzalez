#Name:
#Class: 5th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be given a number as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification

#Code Here:
import math
#ask for height of patient
Height= int(input("What is your height in meters?: "))
#now ask for patients weight
Weight= int(input("Imput your weight in kg: "))
bmi = Weight/(Height**2)

if bmi < 18.5:
    print("You are underweight.")
elif bmi >= 18.5 and bmi <= 24.9:
    print("You are normal weight.")
elif bmi >= 25 and bmi <= 29.9:
    print("You are overweight.")
else :
    print("You are obese.")