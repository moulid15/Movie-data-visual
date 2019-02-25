from bs4 import BeautifulSoup
import requests
import certifi
import pandas

url = 'https://www.boxofficemojo.com/alltime/domestic.htm'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
# print(type(soup.find_all('a')))
name = []
movie = []
money = []
d = dict = {}
delete = 0
names = soup.find("div", {"id": "main"}).find("div", {"id": "body"}).find_all('a')
gross = soup.find("div", {"id": "main"}).find("div", {"id": "body"}).find_all('b')


def todic(list1, list2):
    ret = {}
    for i in range(len(list1)):
        ret[list1[i]] = list2[i]
    return ret


for i in gross:
    if delete == 4:
        movie.append(i.string)
    else:
        delete += 1
movie.remove(movie[-1])
delete = 0
# print(movie)
for i in movie:
    if delete % 2 != 0:
        money.append(i)
    else:
        name.append(i)
    delete += 1
d = todic(name, money)


def ret():
    return d


print(d)
