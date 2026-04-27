from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.service import Service
from datetime import datetime
import pandas as pd
import time


"""
یافتن قیمت ثانیه ای ارز تتر
"""

baseURL = 'https://nobitex.ir/'

# chromeDriver = Service(executable_path='/windows/chromedriver.exe')
# driver = webdriver.Chrome(service=chromeDriver)

driver = webdriver.Chrome(options=Options())
driver.get(baseURL)

prices = []
dates = []
times = []

# XPath=//tagname[@Attribute="Value"]

for i in range(1,11):
    all_price = driver.find_elements(By.XPATH, '//span[@class="text-body-medium tablet:text-body-large desktop:text-body-large"]')
    price = all_price[3]
    now = datetime.now()
    date_str = now.strftime("%m/%d/%Y")
    time_str = now.strftime("%H:%M:%S")

    prices.append(price.text)
    dates.append(date_str)
    times.append(time_str)

    time.sleep(2)
    if i%2==0:
        time.sleep(0.5+i)
    else:
        time.sleep(i-0.5)

driver.quit()

date_frame = pd.DataFrame({'prices':prices, 'times':times, 'dates':dates})
date_frame.to_csv('prices.csv', index=False)
print(date_frame)
