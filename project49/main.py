#you can improve this not so hard jus use api its okay


import requests 
import pywhatkit as kit 


api_url="https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo"
api_key="4DJUXB9FJCHPGWYB"



# api_key="ab0a53e6b193992b66db6677"  # This one gotta be special to you 
# api_url=f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}'

response=requests.get(api_url)
data=response.json()


print(data)



