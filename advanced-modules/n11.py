import requests

from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")

list = soup.find_all("li",{"class":"column"},limit=1)

for li in list:
    name = li.div.div.a.h3.text.strip()
    link = li.div.div.a.get("href")
    oldPrice = li.find("span",{"class":"oldPrice"}).text.strip()
    newPrice = li.find("span",{"class":"newPrice"}).text.strip()
    print(f"Name: {name}\nLink: {link}\nOld price: {oldPrice}\nNew price: {newPrice}")


# print(list)




