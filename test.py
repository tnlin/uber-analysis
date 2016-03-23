import requests
from bs4 import BeautifulSoup
start=14000
end=14100
url = "http://itunes.apple.com/WebObjects/MZStore.woa/wa/userReviewsRow?cc=cn&id=368677368&displayable-kind=11&startIndex="+(str)(start)+"&endIndex="+(str)(end)+"&sort=0&appVersion=all" 
headers = {
    'User-Agent': 'iTunes/11.0 (Windows; Microsoft Windows 7 Business Edition Service Pack 1 (Build 7601)) AppleWebKit/536.27.1',
    'From': 'student@tsinghua.edu.cn'  # This is another valid field
}
#Bug Demo
#f = open('ok.html', 'r')  
#soup = BeautifulSoup(f.read(), "lxml")

r = requests.get(url,headers=headers)
soup = BeautifulSoup(r.content, "lxml")
print (soup)
#f.write(str(soup))
#f.close()
