
'''
GoTo Command Prompt and install speedtest package using command 'pip install speedtest-cli'
After that run the below code to get the internet speed on your console.
'''


import os
os.system('cmd /c "speedtest-cli"')  # Here we are running the console command 'speedtest-cli' using python code



'''
The output will be like-

Retrieving speedtest.net configuration...
Testing from Airtel (223.187.156.60)...
Retrieving speedtest.net server list...
Selecting best server based on ping...
Hosted by NANDBALAJI CONNECTING ZONE PVT. LTD (Godda) [52.57 km]: 133.118 ms
Testing download speed..........................................
Download: 12.68 Mbit/s
Testing upload speed............................................
Upload: 11.69 Mbit/s

Process finished with exit code 0

'''