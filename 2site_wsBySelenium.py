import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import logging
logging.basicConfig(level=logging.INFO)


"""
از جادی: که برای یافتن اولین کتاب یک نویسنده
یافتن نویسندگان با اول اسم س و اول فامیلی ط از سایت ویکی پدیا
یافتن اولین کتابهای این نویسندگان از سایت کتاب
"""

def showOneThing(name):
    try:
        name = urllib.quote_plus(name)
        baseURL = 'http://www.goodreads.com/'
        chromeDriver = Service(executable_path='/windows/chromedriver.exe')
        driver = webdriver.Chrome(service=chromeDriver)
        driver.get(baseURL+'/search?utf8=%E2%9C%938search_type=books&search%5Bfield=outhor&q='+name)
        firstThingURL = driver.find_element(By.XPATH, '//a[@class="bookTitle"]')
        print('"'+baseURL+firstThingURL+'"')
    except:
        pass



chromeDriver = Service(executable_path='/windows/chromedriver.exe')
driver = webdriver.Chrome(service=chromeDriver)
driver.get("http://en.m.wikipedia.org/wiki/List_of_outhors_by_name:_T")
# names = driver.find_elements(By.XPATH, '//*[@id="search"]')
names = driver.find_element(By.XPATH, '//a[@class="outhorName"]')

for i in names:
    if i.string is None:
        continue
    if i.string[0] == 'S' and len(i.string)>1:
        try:
            showOneThing(str(i.string))
            logging.info(i.string)
        except:
            pass

driver.quit()
