'''
step1. GoTo Command Prompt and install pyshorteners package using command 'pip install pyshorteners'
After that run the below code
'''


import pyshorteners

url = input("Enter URL which you want to Shorten : \n")

print("URL After Shortening :- ", pyshorteners.Shortener().tinyurl.short(url)) 
# This above line print the Shorten url of your Entred Long URL.


### End of Code ###

