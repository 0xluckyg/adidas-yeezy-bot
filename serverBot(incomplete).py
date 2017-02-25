# pip install requests
# pip install beautifulsoup4
# pip install lxml
# (instal mac ports and run sudo port install py27-lxml)

import requests
import bs4
import random
import webbrowser
import threading
import RandomHeaders

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
baseURL = 'http://www.adidas.com/us/superstar-primeknit-shoes/S82241.html?forceSelSize=S82241_590'
model = 'CP9654'

# proxies =

modelNumber = 'S82241'
sizeList = [6,7,8,9]
threadCount = 10


def buyShoe():
    print('bought')

def generateURL(model, size):
    baseSize = 580
    shoeSize = size - 6.5
    shoeSize = shoeSize * 20
    rawSize = shoeSize + baseSize
    shoeSizeFinal = int(rawSize)
    return 'http://www.adidas.com/us/' + str(model) + '.html?forceSelSize=' + str(model) + '_' + str(shoeSizeFinal)

def checkStock(url):
    res = requests.get(url, headers = headers);
    page = bs4.BeautifulSoup(res.text, 'lxml');
    rawListOfSizes = page.select('.size-dropdown-block')
    sizes = rawListOfSizes[0].getText().replace('\t', '').split()
    sizes.remove('Select');
    sizes.remove('size');
    print(sizes)
    return sizes

def main(model, size):
    URL = generateURL(model, size);
    checkStock(URL);

def runBot(model, size=None):
    while True:
        try:
            url = 'http://www.adidas.com/us/' + str(model) + '.html?'
            sizes = checkStock(url)
            buyShoe()
            if size != None:
                if str(size) in Sizes:
                    buyShoe()
            else:
                for size in sizes:
                    buyShoe()
        except:
            pass

threads = [threading.Thread(name='ThreadNumber{}'.format(n), target=runBot, args=(modelNumber, size)) for size in sizeList for n in range(threadCount)]

for thread in threads:
    thread.start();

main('S82241', 7)
