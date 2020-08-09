'''
step1. GoTo Command Prompt and install package pyttsx3==2.71 using command 'pip install pyttsx3==2.71'
step2. install package pywin32 using command pip install pywin32

After that run the below code
'''

import pyttsx3

data = input("Enter text which you want to convert to text:\n")

engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()

### End of Code ###
