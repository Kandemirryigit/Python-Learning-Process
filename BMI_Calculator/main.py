# BMI Calculator (Body Mass Index)


# Bmi<=18.4  underweight
# 18.5<Mmi<=24.9 normal
# 25<=Bmi<=39.9 overweight
# Bmi>=40 obese


# wight's unit kg
# height's unit metre



#  import logo1 and logo2 from art.py to main.py ı used this method 
from art import logo1,logo2


# to create an infinitive loop
run=True

# while True
while run:
    print(logo1)

    weight=float(input("can you say your weight(kg)? "))     # Kg
    height=float(input("can you say your height(m)? "))     # m
    bmi=weight/(height*2)    # the formul of BMI

    if bmi<=18.4:
        print("Your body is underweight")
    elif 18.5<bmi and bmi<=24.9:
        print("Your body is normal")
    elif 25<=bmi and bmi<=39.9:
        print("Your body is overweight")
    elif bmi>40:
        print("Your body is obese")

    wanna_contiune=input("do you wanna contiune for another person? y/n: ").lower()
    if wanna_contiune=="n":
            print("\n"*50)  # to show a fresh screen
            print(logo2)
            run=False
    else:
         print("\n"*50)  # to show a fresh screen

