from bs4 import BeautifulSoup
import requests

weeknum = []
week = []
url = 'https://www.boxofficemojo.com/weekly/?view=year&p=.htm'
response = requests.get(url)

soup=BeautifulSoup(response.content, 'html.parser')

names = soup.find("div", {"id": "body"}).find_all('font', face="Arial")
for i in names:
        weeknum.append(i.string)

del (weeknum[0:7])
week = [weeknum[x] for x in range(len(weeknum)) if not x % 8 == 0]

print(week)
