import requests
import re
from bs4 import BeautifulSoup
# soup = BeautifulSoup(requests.get('http://gokifu.com/index.php?p=2&a=1&y=2016&m=1').content, 'lxml')

#urls1 = []


# #for c in soup.findAll("a", href = re.compile("&a=1&y=2016&m=1")):
# #    urls1.append(c.get('href'))
# #    print(len(urls1))
# for i in range(1, 4):
    # soup1 = BeautifulSoup(requests.get('http://gokifu.com/index.php?p=' + str(i) + '&a=1&y=2016&m=1').content, 'lxml')

    # for b in soup1.findAll("a", href = re.compile(".sgf")):
        # urls.append(b.get('href'))

# print(len(urls))
# for i in range(len(urls)):
    # r = requests.get(urls[i], stream=True, verify = False)
    # with open('data\\' + urls[i][len('http://gokifu.com/f/'):], "wb") as code:
         # code.write(r.content)
year = '2017'
for j in range(1, 13):
	urls = []
	url = 'http://gokifu.com/index.php?p=2&a=1&y=' + year + '&m=' + str(j)
	suffix = '&a=1&y=' + year + '&m=' + str(j)
	soup = BeautifulSoup(requests.get(url).content, 'lxml')
	# print(soup)
	# for i in range(1, len(soup.findAll("a", href = re.compile("&a=1&y=2016&m=1"))) - 1):
		# print(i)
	for i in range(1, len(soup.findAll("a", href = re.compile(suffix))) - 1):
		soup1 = BeautifulSoup(requests.get('http://gokifu.com/index.php?p=' + str(i) + suffix).content, 'lxml')

		for b in soup1.findAll("a", href = re.compile(".sgf")):
			urls.append(b.get('href'))

	print(len(urls))
	for i in range(len(urls)):
		r = requests.get(urls[i], stream=True, verify = False)
		with open('data\\' + urls[i][len('http://gokifu.com/f/'):], "wb") as code:
			 code.write(r.content)