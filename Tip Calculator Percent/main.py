#Tip Calculator



#to import our logo to our .py file we are using this method
from art import logo



#to show our logo and text
print(logo)
print("Welcome to the tip calculator.\n")



#we are using this to take input so we are gonna take information from user
#we should use int before input because input's default data type is str but we are gonna make operation with numbers
total_bill=int(input("How much total bill? $"))
total_tip=int(input("how much tip do you wanna give? %"))
number_of_people=int(input("how many people to split the bill? "))
 


#we used this formule to find total price
total_price=(total_bill)*((100+total_tip)/100)


# we used this formule to find how much money each person will pay
#if you wanna see float numbers you can change int to float
each_person_gotta_pay=int(total_price/number_of_people)



#to show final output 
print(f"each person gotta pay: {each_person_gotta_pay}$")
 
