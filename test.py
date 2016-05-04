import requests
from bs4 import BeautifulSoup
cc="us"
start=5350
end=5400
url = "http://itunes.apple.com/WebObjects/MZStore.woa/wa/userReviewsRow?cc="+cc+"&id=368677368&displayable-kind=11&startIndex="+(str)(start)+"&endIndex="+(str)(end)+"&sort=0&appVersion=all"
headers = {
    'User-Agent': 'iTunes/11.0 (Windows; Microsoft Windows 7 Business Edition Service Pack 1 (Build 7601)) AppleWebKit/536.27.1',
    'From': 'student@tsinghua.edu.cn'  # This is another valid field
}

f = open('test.html', 'w')  
r = requests.get(url,headers=headers)
content = bytes(r.text.replace('<',''), encoding = "utf8")
#print (c1)
soup = BeautifulSoup( content , "lxml")
print (soup.text)
f.write(soup.text)
f.close()
#print (json.dumps(data, indent=4,ensure_ascii=False))#json.dump default use ascii
