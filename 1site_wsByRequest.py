from datetime import datetime
import time
import requests
import bs4
import pandas as pd


"""
یافتن قیمت ثانیه ای ارز تتر
"""

baseURL = 'https://nobitex.ir/'

page = requests.get(baseURL)
soup = bs4.BeautifulSoup(page.content)

prices = []
dates = []
times = []
for i in range(1,11):
    all_price = soup.find_all('span', class_='text-body-medium tablet:text-body-large desktop:text-body-large')
    price = all_price[3]

    now = datetime.now()
    date_str = now.strftime("%m/%d/%Y")
    time_str = now.strftime("%H:%M:%S")

    prices.append(price.text)
    dates.append(date_str)
    times.append(time_str)

    time.sleep(1)
    if i % 2 == 0:
        time.sleep(0.5 + i)
    else:
        time.sleep(i - 0.5)


date_frame = pd.DataFrame({'prices':prices, 'times':times, 'dates':dates})
date_frame.to_csv('prices.csv', index=False)
print(date_frame)
