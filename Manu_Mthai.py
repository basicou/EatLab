import requests
from bs4 import BeautifulSoup

wording = input("Please Fill Manu:")
beginurl = "https://cooking.kapook.com/menu"
pagemain = requests.get(beginurl)
soupmain = BeautifulSoup(pagemain.content,"html.parser")
endurl = soupmain.find_all('a')
i = 0
while i < len(endurl):
    try:
        if endurl[i].find('h3').get_text() == wording:
            endurl = endurl[i].get('href')
    except:
        pass
    i = i + 1

totalurl = endurl
print(totalurl)

pagesub = requests.get(totalurl)
soupsub = BeautifulSoup(pagesub.content, 'html.parser')
recipe = soupsub.find_all('div', class_='tp_text-2')

i = 0
b = []
while i < len(recipe):
    a = []
    try:
        a = recipe[i].find_all('li')
        b += a
    except:
        pass
    i = i + 1

recipe = b

i = 0
while i < len(recipe):
    print(recipe[i].get_text())
    i = i +1