from bs4 import BeautifulSoup
import requests

weeknum='09'

url='https://www.boxofficemojo.com/weekly/chart/?yr=2019&wk='+str(weeknum)+'&p=.htm'
response= requests.get(url)

soup=BeautifulSoup(response.content,'html.parser')

names = soup.find("div", {"id": "main"}).find("div", {"id": "body"}).find('table',).findall('b')
gross = soup.find("div", {"id": "main"}).find("div", {"id": "body"}).find_all('font')

print(names)