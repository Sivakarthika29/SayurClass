#Calculate the BMI and if the person is underweihgt/normal/overweight/obese

name=input("Enter your name: ")
age=int(input("Enter your age: "))
gender=input("Enter your gender: ")
#getting weight in kg
weight=float(input("Enter your weight in kg: "))
#getting weight in cm
height=float(input("Enter your height in cm: "))
bmi=weight/(height/100)**2
print("Name: ",name)
print("Age: ",age)
print("Gender: ",gender)
print("Your Body Mass index is ",bmi)
if bmi < 18.5:
    print("You are Underweight")
elif bmi <= 24.9:
    print("You are Normal")
elif bmi <= 29.9:
    print("You are Overweight")
else:
    print("You are Obese")
    
if(age<20 and bmi<18.5):
    print("Have some fruits to gain weight")
if(age>60 and bmi>24.9):
    print("Have a regular workout")
if(age>10 and bmi>30):
    print("You need to have strict excercies")


# OUTPUT:

# Enter your name: Sivakarthika
# Enter your age: 19
# Enter your gender: Female
# Enter your weight in kg: 49
# Enter your height in cm: 165
# Name:  Sivakarthika
# Age:  19
# Gender:  Female
# Your Body Mass index is  17.99816345270891
# You are Underweight
# Have some fruits to gain weight