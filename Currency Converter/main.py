# Tkinters for user interface
import tkinter as tk
from tkinter import ttk
import requests  # To send HTTP requests to interact with web services, APIs, or fetch web pages.
from tkinter import messagebox  # To show pop-up in the screen

window=tk.Tk() # to define tkinter
window.title("Currency Converter")  # To determine window's title
window.minsize(400,300)  # To determine window's size
window.config(bg="#524C42") # To determine window's background color

# To creat texts and determine their location,background and foreground color,font
currency_converter_title=tk.Label(text="Currency Converter",font=("Monospace",20,"bold"),bg="#524C42",fg="#E2DFD0")
currency_converter_title.grid(column=1,row=1)

convert_text=tk.Label(text="Convert:",fg="#E2DFD0",bg="#524C42",font=("Monospace",18,"bold"))
convert_text.grid(column=0,row=2,pady=30)

result_text=tk.Label(text="Result:",fg="#E2DFD0",bg="#524C42",font=("Monospace",18,"bold"))
result_text.grid(column=0,row=5)

result=tk.Label(text="-",fg="#E2DFD0",bg="#524C42",font=("Monospace",18,"bold"))
result.grid(column=1,row=5)

to_text=tk.Label(text="To:",fg="#E2DFD0",bg="#524C42",font=("Monospace",18,"bold"))
to_text.grid(column=0,row=3)


# To create an input and determine it's location
first_number_entry=tk.Entry()
first_number_entry.focus()  # To create a blinking cursor in the input
first_number_entry.grid(column=1,row=2)

# To set a default value
unit1=tk.StringVar()
unit1.set("USD")

unit2=tk.StringVar()
unit2.set("TRY")


# To define all currencies
currencies=[
'USD','EUR','JPY','GBP','AUD','CAD','AED','AFN','ALL','AMD','ANG','AOA','ARS','AWG' ,'AZN' ,'BAM','BBD','BDT','BGN','BHD' ,'BIF','BMD','BND',
'BOB','BRL','BSD','BTN','BWP','BYN','BZD','CDF','CHF','CLP' ,'CNY' ,'COP' ,'CRC' ,'CUP','CVE','CZK' 'DJF',
'DKK','DOP','DZD','EGP' ,'ERN','ETB','FJD' ,'FKP','FOK','GEL','GGP','GHS','GIP' ,'GMD','GNF','GTQ',
'GYD','HKD','HNL' ,'HRK' ,'HTG','HUF','IDR','ILS','IMP','INR' ,'IQD' ,'IRR' ,'ISK' ,'JEP' ,'JMD' ,'JOD','KES',
'KGS' ,'KHR' ,'KID','KMF' ,'KRW','KWD','KYD','KZT','LAK' ,'LBP','LKR' ,'LRD' ,'LSL' ,'LYD','MAD','MDL','MGA' ,'MKD'
'MMK','MNT' ,'MOP','MRU','MUR' ,'MVR' ,'MWK' ,'MXN','MYR','MZN' ,'NAD','NGN','NIO' ,'NOK' ,'NPR','NZD','OMR','PAB'
'PEN','PGK','PHP','PKR','PLN','PYG','QAR' ,'RON','RSD','RUB','RWF','SAR','SBD' ,'SCR','SDG','SEK','SGD','SHP','SLE'
'SLL' ,'SOS' ,'SRD' ,'SSP' ,'STN','SYP' ,'SZL','THB' ,'TJS','TMT','TND' ,'TOP' ,'TRY','TTD','TVD' ,'TWD','TZS' ,'UAH'
'UGX' ,'UYU' ,'UZS' ,'VES','VND','VUV' ,'WST' ,'XAF' ,'XCD','XDR','XOF','XPF','YER' ,'ZAR','ZMW','ZWL']

# To create a menu 
unit1_menu = ttk.Combobox(window, textvariable=unit1, values=currencies, state="normal")
unit1_menu.grid(column=2,row=2)

unit2_menu=ttk.Combobox(window,textvariable=unit2,values=currencies,state="normal")
unit2_menu.grid(column=1,row=3)

# To add point(.) after every 3 chracters.Because its much more readable
def format_number_with_dots(number):
    return "{:,}".format(number).replace(",", ".")

# To convert every single currency properly
def convert(): 

    # If you don't write anything or you don't write number you are gonna see a pop-up in the screen
    try:
        amount=float(first_number_entry.get())
    except ValueError:
        messagebox.showinfo(title="Oooppsss",message="Please write a valid number.")

    base_currency=unit1_menu.get()
    target_currency=unit2_menu.get()

    api_key="ab0a53e6b193992b66db6677"  # This one gotta be special to you 
    url=f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}'

    response=requests.get(url)
    data=response.json()  # To convert json format
    
    if response.status_code==200:  # If it works
        rates=data["conversion_rates"]  # more detail
        if target_currency in rates:
            end=amount*rates[target_currency]  # Math to find result 
            formatted_end = format_number_with_dots(round(end, 2))
            result.config(text=f"{formatted_end} {unit2_menu.get()}")     

    
# To creat button and give it a loction,width value,command
convert_button=tk.Button(text="Convert",width=30,command=convert)
convert_button.grid(column=1,row=4,pady=30)

window.mainloop()  # If I don't click exit button the screen won't close
