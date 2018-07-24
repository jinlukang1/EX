import requests
import re
from bs4 import BeautifulSoup
import wget

for i in range(2004, 2005):
	urls = []
	url = 'http://data.remss.com/sst/daily/mw/v05.0/bmaps/' + str(i) + '/'
	soup = BeautifulSoup(requests.get(url).content, 'lxml')
#	print(soup)
#	print(soup.findAll("a", href = re.compile('/sst/daily/mw/v05.0/bmaps/')))
	for j in soup.findAll("a", href = re.compile('/sst/daily/mw/v05.0/bmaps/')):
#		for b in soup.findAll("a", href = re.compile('/sst/daily/mw/v05.0/bmaps/')):
			urls.append('http://data.remss.com' + j.get('href'))

	print(len(urls))
	for i in range(302, len(urls)):
		wget.download(urls[i], urls[i][len('http://data.remss.com/sst/daily/mw/v05.0/bmaps/1998/'):])
#		r = requests.get(urls[i], stream = True, verify = False)
#		with open('data/' + urls[i][len('http://data.remss.com/sst/daily/mw/v05.0/bmaps/1998/'):], "wb") as nc:
#			 nc.write(r.content)
