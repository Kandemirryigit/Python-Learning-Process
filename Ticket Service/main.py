#Rollercoaster Ticket Service


#to import our logos from art.py to main.py we are using this method
from art import logo1,logo2



#this is the another else method to import logo1 and logo2 but in my opinion not useful
# from art import logo1
# from art import logo2


#to create infinitive loop run is equal True 
run=True


#while run means while True
while run:
    print(logo1)
    print('welcome to ticket service')
    print("you can see the ticket prices below\n \n18<=age<45 and 55<age: 20$\n12<=age<18: 10$\nage<12: 5$\n45<=age<=55: 0$\n")
    height=int(input('can you say your height? '))  
   

    if height>=120:      
        age=int(input("can you say your age? "))

        if 18<=age and age<45:
            bill=+20
            print(f"your total bill: {bill}$")
        if 12<=age<18:
            bill=+10
            print(f"your total bill: {bill}$")
        if age<=12:
            bill=+5
            print(f"your total bill: {bill}$")
        if 45<=age<=55:
            bill=+0
            print(f"your total bill: {bill}$")

        #ı added lower() method because of that Y=y or N=n
        wanna_contiune=input("do you wanna contiune to other persons? y/n: ").lower()
        if wanna_contiune=="n":
            print("\n"*50) #to show a fresh screen
            print(logo2)
            run=False #the loop is over
        else:
            print("\n"*50)
             
    else:
        print("Sorry you can't use rollercoaster because of your height")
        #ı added lower() method because of that Y=y or N=n
        question=input("do you wanna  calculate for another person? Y/N: ").lower()
        if question=="n":
            print("\n"*50)
            print(logo2)
            run=False #the loop is over
        else:
            print("\n"*50)
        
      
           


       
       

    
        