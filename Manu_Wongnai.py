import requests
from bs4 import BeautifulSoup

wording = input("Please Fill Manu:")
beginurl = "https://www.wongnai.com/cooking"
pagemain = requests.get(beginurl)
soupmain = BeautifulSoup(pagemain.content,"html.parser")
endurl = soupmain.find('a',href=True, text= wording).get('href')
totalurl =  beginurl[0:24]+ endurl
print(totalurl)

pagesub = requests.get(totalurl)
soupsub = BeautifulSoup(pagesub.content, 'html.parser')
recipe = soupsub.find('div', class_='_6wPoUEcyGHyKclHBkNIvM _2siCsDLJkCSdW5cVuajRYN').find_all('li')

i = 0
while i < len(recipe):
    print(recipe[i].get_text())
    i = i + 1