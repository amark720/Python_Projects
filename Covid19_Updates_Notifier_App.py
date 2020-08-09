'''
GoTo Command Prompt and install requests package using command 'pip install requests'
and install win10toast package using command 'pip install win10toast'.
After that run the below code to get the worldwide CoVid19 cases update on your windows notification area.
'''

import requests #To handle Api calls
from win10toast import ToastNotifier #for showing windows notification toast
import json
import time

def update():
    r= requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data = r.json() #converting/typecasting the get request into Json format.
    text = f'Confirmed Cases : {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}'
    #The above is the text which will be printed onto the notification window area.

    while True:
        toast = ToastNotifier()
        toast.show_toast("Covid-19 Updates",text,duration=20)  # Duration 20 sec means the notification will disappear in 20 seconds
        time.sleep(600) # Time accepted in seconds after each interval new updated notification will come.


update() #calling the update function

### End of Code ###
