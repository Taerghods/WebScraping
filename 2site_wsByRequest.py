import urllib
import requests
import bs4
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
        page = requests.get(baseURL+'/search?utf8=%E2%9C%938search_type=books&search%5Bfield=outhor&q='+name)
        soup = bs4.BeautifulSoup(page.content)
        firstThingURL = soup.find('a', 'bookTitle')['href']
        print('"'+baseURL+firstThingURL+'"')
    except:
        pass


page = requests.get("http://en.m.wikipedia.org/wiki/List_of_outhors_by_name:_T")
soup = bs4.BeautifulSoup(page.content)
names = soup.findAll('a')

for i in names:
    if i.string is None:
        continue
    if i.string[0] == 'S' and len(i.string)>1:
        try:
            showOneThing(str(i.string))
            logging.info(i.string)
        except:
            pass
