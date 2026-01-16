from tkinter import *  # From tkinter import everything
import requests  # to send HTTP/HTTPS requests
from tkinter import messagebox  # To show pop-up in the screen

# You can change this variables
PASSWORD=1903  
remaind=4
money=1000


def main_window_func():  # Main window

    main_window=Tk()
    main_window.minsize(500,400)
    main_window.title("Menü")
    main_window.config(bg="red")

    welcome_text=Label(text="Welcome to X bank",font=("Monospace",24,"bold"),bg="red",fg="white")
    welcome_text.place(x=100,y=50)

    def exit_clicked():
        main_window.destroy()

    exit_button=Button(text="Exit",fg="black",bg="white",font=("Monospace",12,"bold"),command=exit_clicked,width=10)
    exit_button.place(x=400,y=350)

    # Withraw money window
 
    def withdraw_money_clicked():  
       
        main_window.destroy()
        withdraw_window=Tk()
        withdraw_window.title("withdraw Money")
        withdraw_window.minsize(400,400)
        withdraw_window.config(bg="red")

        how_much_money_text=Label(text="How Much Money You Wanna take",font=("Monospace",15,"bold"),bg="red",fg="white")
        how_much_money_text.place(x=30,y=50)

        withdraw_money_enter=Entry(width=20,font=("Monospace",15,"bold"))
        withdraw_money_enter.focus()  # To add a blinking cursor
        withdraw_money_enter.place(x=85,y=140)

        def ok_clicked():  # If I click ok button
            # I'm inside a function and if I wanna use this variable I should use this global method
            global money  
            try:  # Run the code
                withdraw_price=int(withdraw_money_enter.get())
            except ValueError:  # If you see valueError
                messagebox.showinfo(title="Oppsss",message="you should write number.")
            money-=withdraw_price
            withdraw_window.destroy() 
            main_window_func()
           
        ok_button=Button(text="Ok",fg="white",bg="black",font=("Monospace",12,"bold"),height=2,width=10,command=ok_clicked)
        ok_button.place(x=150,y=200)

        def back_clicked():  # If I click back button
            withdraw_window.destroy()
            main_window_func()

        back_button=Button(text="Back",fg="black",bg="white",font=("Monospace",12,"bold"),command=back_clicked)
        back_button.place(x=350,y=350)

        withdraw_window.mainloop()


    withdraw_money_button=Button(text="Withdraw Money",fg="white",bg="black",
                                 font=("Monospace",12,"bold"),height=3,width=20,command=withdraw_money_clicked)
    withdraw_money_button.place(x=0,y=150)

    # Deposit money window

    def deposit_money_clicked():
       
        main_window.destroy()
        deposit_window=Tk()
        deposit_window.title("Deposit Money")
        deposit_window.minsize(400,400)
        deposit_window.config(bg="red")

        how_much_money_text=Label(text="How Much Money You Wanna give",font=("Monospace",15,"bold"),bg="red",fg="white")
        how_much_money_text.place(x=30,y=50)

        deposit_money_enter=Entry(width=20,font=("Monospace",15,"bold"))
        deposit_money_enter.focus()
        deposit_money_enter.place(x=85,y=140)

        def ok_clicked():  # If I click ok button
            global money
            try:
                deposit_price=int(deposit_money_enter.get())
            except ValueError:
                messagebox.showinfo(title="Oppsss",message="you should write number.")
            money+=deposit_price
            deposit_window.destroy()
            main_window_func()
           
        ok_button=Button(text="Ok",fg="white",bg="black",font=("Monospace",12,"bold"),height=2,width=10,command=ok_clicked)
        ok_button.place(x=150,y=200)

        def back_clicked():
            deposit_window.destroy()
            main_window_func()

        back_button=Button(text="Back",fg="black",bg="white",font=("Monospace",12,"bold"),command=back_clicked)
        back_button.place(x=350,y=350)

        deposit_window.mainloop()

    deposit_money_button=Button(text="Deposit Money",fg="white",bg="black",font=("Monospace",12,"bold"),
                                height=3,width=20,command=deposit_money_clicked)
    deposit_money_button.place(x=0,y=250)

    # check balance window

    def check_balance_clicked():
        main_window.destroy()
        price_window=Tk()
        price_window.config(bg="red")
        price_window.minsize(300,300)
        price_window.title("Box")

        money_text=Label(text=f"Money: {money} TRY",font=("Monospace",15,"bold"),bg="red",fg="white")
        money_text.place(x=70,y=120)

        def back_clicked():
            price_window.destroy()
            main_window_func()

        back_button=Button(text="Back",fg="black",bg="white",font=("Monospace",12,"bold"),command=back_clicked)
        back_button.place(x=250,y=260)

        price_window.mainloop()

    check_balance_button=Button(text="Check Balance",fg="white",bg="black",font=("Monospace",12,"bold"),
                                height=3,width=20,command=check_balance_clicked)
    check_balance_button.place(x=300,y=150)

    # Exchange window

    def exchange_clicked():
        api_key="ab0a53e6b193992b66db6677"  # This one gotta be special to you 
        urls=["TRY","USD","EUR","JPY","GBP","AUD","CAD","CHF","HKD","NZD"]
        prices=[]

        for url in urls:
            endpoint=f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{url}'
            response=requests.get(endpoint)
            data=response.json()  # to convert response json type
            price=data["conversion_rates"]["TRY"]
            prices.append(price)

        main_window.destroy()
        exchange_window=Tk()
        exchange_window.minsize(400,400)
        exchange_window.config(bg="red")
        exchange_window.title("Exchanges")

        # to create texts
        
        exchanges_text=Label(text="Exchanges",font=("Monospace",24,"bold"),bg="red",fg="black")
        exchanges_text.place(x=100,y=10)

        try_text=Label(text=f"TRY: {prices[0]}",font=("Monospace",15,"bold"),bg="red",fg="white")
        try_text.place(x=2,y=140)

        # :.2f means show 2 chracters after point in float numbers

        usd_text=Label(text=f"USD: {prices[1]:.2f}",font=("Monospace",15,"bold"),bg="red",fg="white")
        usd_text.place(x=2,y=180)

        eur_text=Label(text=f"EUR: {prices[2]:.2f}",font=("Monospace",15,"bold"),bg="red",fg="white")
        eur_text.place(x=2,y=220)

        jpy_text=Label(text=f"JPY: {prices[3]:.2f}",font=("Monospace",15,"bold"),bg="red",fg="white")
        jpy_text.place(x=2,y=260)

        gbp_text=Label(text=f"GBP: {prices[4]:.2f}",font=("Monospace",15,"bold"),bg="red",fg="white")
        gbp_text.place(x=2,y=300)

        aud_text=Label(text=f"AUD: {prices[5]:.2f}",font=("Monospace",15,"bold"),bg="red",fg="white")
        aud_text.place(x=260,y=140)

        cad_text=Label(text=f"CAD: {prices[6]:.2f}",font=("Monospace",15,"bold"),bg="red",fg="white")
        cad_text.place(x=260,y=180)

        chf_text=Label(text=f"CHF: {prices[7]:.2f}",font=("Monospace",15,"bold"),bg="red",fg="white")
        chf_text.place(x=260,y=220)

        hkd_text=Label(text=f"HKD: {prices[8]:.2f}",font=("Monospace",15,"bold"),bg="red",fg="white")
        hkd_text.place(x=260,y=260)

        nzd_text=Label(text=f"NZD: {prices[9]:.2f}",font=("Monospace",15,"bold"),bg="red",fg="white")
        nzd_text.place(x=260,y=300)

        def back_clicked():
            exchange_window.destroy()
            main_window_func()

        back_button=Button(text="Back",fg="black",bg="white",font=("Monospace",12,"bold"),command=back_clicked)
        back_button.place(x=350,y=350)

        exchange_window.mainloop()

    view_exchange_rates_button=Button(text="View Exchange Rates",fg="white",bg="black",font=("Monospace",12,"bold"),height=3,width=20,command=exchange_clicked)
    view_exchange_rates_button.place(x=300,y=250)

    main_window.mainloop()


# Log-in window

def on_check():
    if check_var.get()==0:
        password_enter.config(show="*")  # Hide password
    else:
        password_enter.config(show="")   # Show password
        

def login_window():
    # I'm inside a function and if I want to use this variables I should use this method
    global check_var,password_enter,remaind
   
    login_window=Tk()
    login_window.maxsize(500,400)
    login_window.minsize(500,400)
    login_window.config(bg="red")
    login_window.title("Welcome ATM")

    please_enter_pass_text=Label(text="Please Enter your Password",font=("Monospace",24,"bold"),bg="red",fg="white")
    please_enter_pass_text.place(x=30,y=80)

    check_var=IntVar(value=0)  # Default value is 0
    checkbutton=Checkbutton(text="Show Password",width=10,bg="gray",fg="black",variable=check_var,command=on_check)
    checkbutton.place(x=400,y=173)

    password_enter=Entry(width=30,font=("Monospace",15,"bold"))
    password_enter.focus()
    password_enter.place(x=50,y=170)

    on_check()

    def ok_clicked():
        global remaind
        if str(password_enter.get())=="1903":
            login_window.destroy()
            main_window_func()
        else:
            remaind-=1
            wrong_password_text=Label(text="Wrong password,Please Try Again...",font=("Monospace",12,"bold"),bg="red",fg="white")
            wrong_password_text.place(x=110,y=330)

            remaind_text=Label(text=f"Remaind: {remaind}/3",font=("Monospace",12,"bold"),bg="red",fg="white")
            remaind_text.place(x=200,y=350)

            if remaind==0:
               login_window.destroy()
               information_window=Tk()
               information_window.maxsize(500,400)
               information_window.minsize(500,400)
               information_window.config(bg="black")
               information_window.title("Information")

               number_text=Label(text="Contact us: +90 1234567890",font=("Monospace",12,"bold"),bg="black",fg="white")
               number_text.place(x=2,y=10)
               
               information_text=Label(text="We took your card because we dedected something wrong.\n Please talk to our bank.\nWe can't procces your operation here anymore",font=("Monospace",12,"bold"),bg="black",fg="white")
               information_text.place(x=30,y=120)

               def ok2_clicked():
                   information_window.destroy()

               ok_button2=Button(text="Okay",bg="black",fg="white",font=("Monospace",18,"bold"),command=ok2_clicked)
               ok_button2.place(x=200,y=250)

               information_window.mainloop()
  
    ok_button=Button(text="Okay",bg="black",fg="white",font=("Monospace",18,"bold"),command=ok_clicked)
    ok_button.place(x=305,y=230)

    def cancel_clicked():
        login_window.destroy()

    cancel_button=Button(text="Cancel",bg="black",fg="white",font=("Monospace",18,"bold"),command=cancel_clicked)
    cancel_button.place(x=50,y=230)

    login_window.mainloop()

login_window()























