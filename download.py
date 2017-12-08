import requests
from bs4 import BeautifulSoup
soup = BeautifulSoup(requests.get('https://u-go.net/gamerecords/').content, 'lxml')
urls = []
for b in soup.table.findAll('a'):
    urls.append(b.get('href'))
i = 0
print(range(len(urls)))
for i in range(len(urls)):
    r = requests.get(urls[i], stream=True, verify = False)
    with open(urls[i][len('https://dl.u-go.net/gamerecords/'):], "wb") as code:
         code.write(r.content)


urls = []
for b in soup.findAll("a", href = re.compile(".sgf")):
    urls.append(b.get('href'))

i = 0
print(range(len(urls)))
for i in range(len(urls)):
    r = requests.get(urls[i], stream=True, verify = False)
    with open(urls[i][len('http://gokifu.com/index.php?p=3&a=1&y=2016&m=2'):], "wb") as code:
         code.write(r.content)