
#Pizza Order

# small pizza (s): 15$
# medium pizza (m): 20$
# large pizza (l): 25$
# pepperoni for small pizza: +2$
# pepperoni for medium or large pizza: +3$
# add ekstra cheese for any pizza: +1$



# to import time modul
import time
# to import logos from art.py to main.py
from art import pizza,pepperonni,cheese,total,question,byebye


# To create an infinitive loop
wanna_order=True

# While True
while wanna_order:

    print(pizza) # To show pizza logo
    print('Welcome to Python pizza order screen\n')
    print("Small pizza(s): 15$\nMedium pizza(m): 20$\nLarge pizza(l): 25$\n")
    size=input('which size pizza do you want (s,m,l)?: ').lower()   # S->s , M->m , L->l because I added .lower() method

    print("\n"*50) # To create a fresh screen
    print(pepperonni)  # to show Pepperonni logo
    print("Pepperoni for small pizza: +2$\npepperoni for medium and large pizza: +3$\n")
    pepperoni=input('Do you want pepperoni on your pizza? y/n ').lower() # Y->y, N->n because I added .lower() method

    print("\n"*50) # To create a fresh screen
    print(cheese)  # To show cheese logo
    print("Ekstra cheese for any pizza: +1$")
    extra_cheese=input("Do you want extra cheese (y/n)? ").lower()  # Y->y , N->n because I added .lower() method


    if size=="s":
        first_bill=15
    if size=="m":
        first_bill=20
    if size=="l":
        first_bill=25



    if size=="s" and pepperoni=="y":
        second_bill=first_bill+2
    elif size=="s" and pepperoni=="n": 
        second_bill=first_bill
    

    if size=="m" and pepperoni=="y":
        second_bill=first_bill+3
    elif size=="m" and pepperoni=="n":
        second_bill=first_bill
    

    if size=="l" and pepperoni=="y":
        second_bill=first_bill+3
    elif size=="l" and pepperoni=="n":
        second_bill=first_bill
    

    if extra_cheese=="y":
        last_bill=second_bill+1
    elif extra_cheese=="n":
        last_bill=second_bill
    


    print("\n"*50)  # To create a fresh screen
    print(total)  # to show total logo
    print(f"your price is {last_bill}")  # I used f-string method
    my_time=3
    for i in range(my_time,0,-1):   # range(start 3,to 0,count -1)
        print(i)
        time.sleep(1)  # it means wait 1 second and start count after that.so slepp 1 second


    print("\n"*50)  # To create a fresh screen
    print(question)  # To show question logo
    order=input("Do you wanna order another pizza? y/n: ").lower() # Y->y , N->n because I added .lower() method
    if order=="n":
        wanna_order=False  # to stop the loop
        print("\n"*50)   # To create a fresh screen
        print(byebye)
    else:
        print("\n"*50)   # To create a fresh screen







