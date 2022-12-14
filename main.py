import requests
from bs4 import BeautifulSoup

urlList = [
    'https://www.amazon.de/Python-Programmieren-f%C3%BCr-Anf%C3%A4nger-Schritt-f%C3%BCr-Schritt-Anleitungen/dp''/B0B7CR66J2/ref=sr_1_1?keywords=python+programmieren+f%C3%BCr+anf%C3%A4nger&qid=1664736500&qu''=eyJxc2MiOiIyLjg0IiwicXNhIjoiMi41NSIsInFzcCI6IjIuMjYifQ%3D%3D&sprefix=python+programmier%2Caps%2C91&sr=8-1 ',
    'https://www.amazon.de/Automate-Boring-Stuff-Python-2nd/dp/1593279922/ref=''sr_1_1?keywords=automate+the+boring+stuff+with+python&qid=1664744667&qu=''eyJxc2MiOiIxLjg1IiwicXNhIjoiMS45NyIsInFzcCI6IjEuNjQifQ%3D%3D&sprefix=automate+the+%2Caps%2C114&sr=8-1',
    'https://www.amazon.de/Pragmatic-Programmer-journey-mastery-Anniversary/dp/0135957052/ref=sr_1_1?''keywords=the+pragmatic+programmer&qid=1664744779&qu=eyJxc2MiOiIxLjkyIiwicXNhIjoiMS4xNCIsInFzcCI6IjEuMDAifQ%3D%3D&sprefix=the+pragmatic%2Caps%2C90&sr=8-1'
]
###################################################################################
###         THIS DATA IS FOUND IN 'https://httpbin.org/get'                     ###
###         User-Agent needs to be replaced with your data                      ###
###################################################################################

# "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
# "Accept-Encoding": "gzip, deflate, br","Dnt": "1", "Upgrade-Insecure-Requests": "1", "Connection":"close",
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"

myHeaders = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
             "Accept-Encoding": "gzip, deflate, br",
             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
             "Dnt": "1",
             "Upgrade-Insecure-Requests": "1"}


def requestWebsite(URL):
    return requests.get(URL, headers=myHeaders)


def parseWebsite(websiteOfProduct):
    return BeautifulSoup(websiteOfProduct.content, "html.parser")


def getTitleFormProduct(contentOfWebsite):
    return contentOfWebsite.find(id="productTitle").get_text()


def fetchPriceFromProduct(parsedWebsite):
    return parsedWebsite.find(id="price").get_text()


def fetchTitleFromProduct(parsedWebsite):
    title = parsedWebsite.find(id="productTitle").get_text()
    StringEndIndex = title.index(':')  # Get the index of the first ':' that's found in the String
    return title[1:StringEndIndex]  # Use the index to slice the String accordingly


# Loop through every URL in URL_List
for productUrl in urlList:
    siteContent = requestWebsite(productUrl)
    parsedWebsite = parseWebsite(siteContent)
    title = fetchTitleFromProduct(parsedWebsite)
    price = fetchPriceFromProduct(parsedWebsite)
    print(f'{title}: {price}')
