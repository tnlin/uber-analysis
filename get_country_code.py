from bs4 import BeautifulSoup
import requests
url="https://www.apple.com/choose-your-country/"
r  = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")


for row in soup.findAll( 'li' ):
	if row.a:
		print (row.a.text)
	if row.a.span:
		print (row.a.span.text)

#print (soup.prettify())