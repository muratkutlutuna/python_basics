html_doc = """<!doctype html>
<html lang="en">
<head>
    <meta charset="<UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Ilk web sayfam</title>
</head>
<body>
    <h1 is="header">
        Python Kursu
    </h1>

    <h2>
        Programlama
    </h2>

    <div class="grup1"> grup1</div>
    <div class="grup1">
         <ul>
        <li>Menu 1</li>
        <li>Menu 2</li>
        <li>Menu 3</li>
    </ul>
     grup1</div>

    <a href="http://www.bob.com/">success</a>
    <a href="http://www.bob.com/plasma">experiments</a>
    <a href="http://www.boogabooga.net/">BoogaBooga</a>

    <img src="https://st4.depositphotos.com/23658156/29450/i/1600/depositphotos_294505724-stock-photo-macro-shot-many-tiny-tortoise.jpg"
         alt="afide">
</body>
</html>"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')
result = soup.prettify()
result = soup.title
result = soup.head
result = soup.body

result = soup.title.name
result = soup.title.string

result = soup.h1
result = soup.h2
result = soup.h2.name
result = soup.h2.string

result = soup.findAll('h1')
result = soup.findAll('h1')[0]
# result = soup.findAll('h1')[1]
result = soup.findAll('div')
result = soup.findAll('div')[1]
result = soup.findAll('div')[1].ul
result = soup.findAll('div')[1].ul.findAll('li')[2].string

result = soup.div.findChildren()
result = soup.div.findNextSibling().findChildren()
result = soup.div.findNextSibling().findNextSibling().findChildren()

result = soup.find_all('a')

for link in result:
    print(link.get('href'))