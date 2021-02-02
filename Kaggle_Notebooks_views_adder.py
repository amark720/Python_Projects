
'''
GoTo Command Prompt and install selenium package using command 'pip install selenium'
and install humanfriendly package using command 'pip install humanfriendly'.
Update the Kaggle Notebook Post link into the "Link" Variable and set the number of Views you want
Downloaded the latest ChromeDriver.exe from this link - (https://chromedriver.chromium.org/downloads) and after
downloading, extract it and keep that Chromedriver.exe into the same folder from where you're running this Python file.
After that run the below code and wait till the views are getting added.
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
from random import randint
from humanfriendly import format_timespan
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

start_time = time.time()

# ----------------------------------- Update Link and Views Count Below -------------------------------

link = "https://www.kaggle.com/carlmcbrideellis/jane-street-eda-of-day-0-and-feature-importance"  # Change the Kaggle Notebook Link Here.
limit = 20  # Update how many views you want on your post.

# ------------------------------------------------------------------------------------------------------

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)
wait1 = WebDriverWait(driver, 7)
driver.get(link)
driver.maximize_window()
time.sleep(5)

for i in range(0, limit):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_experimental_option("detach", True)
    driver1 = webdriver.Chrome(options=chrome_options)
    wait_incognito = WebDriverWait(driver1, 30)
    driver1.maximize_window()
    driver1.get(link)
    time.sleep(10)
    wait_incognito.until(EC.element_to_be_clickable((By.XPATH,'(//*[@title ="Input"])[1]'))).click()
    time.sleep(10)
    wait_incognito.until(EC.element_to_be_clickable((By.XPATH, '(//*[@title ="Comments"])[1]'))).click()
    time.sleep(10)
    driver1.close()
    print("Completed "+str(i+1) +" Click!!")

end_time = time.time() - start_time
print("Total execution time: ", format_timespan(end_time))
