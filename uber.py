import requests,json,sqlite3,time
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'iTunes/11.0 (Windows; Microsoft Windows 7 Business Edition Service Pack 1 (Build 7602)) AppleWebKit/536.27.1',
    'From': 'ta@nctu.me'  # This is another valid field
}

#sqlite connect
conn = sqlite3.connect('uber.sqlite')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS Uber
  (rating integer, name text, userReviewId text, title text, body text, date text, 
  	voteSum integer, voteCount integer, voteUrl text, viewUsersUserReviewsUrl text, customerType text, cc text)''')
#~10279
cc="us"
flag=True
start=0
end=100
while flag:
	try:
		url = "http://itunes.apple.com/WebObjects/MZStore.woa/wa/userReviewsRow?cc="+cc+"&id=368677368&displayable-kind=11&startIndex="+(str)(start)+"&endIndex="+(str)(end)+"&sort=0&appVersion=all" 
		r = requests.get(url,headers=headers)
		soup = BeautifulSoup(r.content, "html5lib")
		#print (soup)
		jsonResponse = json.loads(str(soup)[25:-14])
		jsonData = jsonResponse["userReviewList"]
		#print (len(jsonData))
		#if (end)==1500:
		if len(jsonData)<100:
			flag=False
		for key,item in enumerate(jsonData):
			print (start+key+1,"|",item.get("rating"),item.get("name"),item.get("title"))
			payloads = [item.get("rating"),item.get("name"),item.get("userReviewId"),item.get("title"),item.get("body"),item.get("date"),\
						item.get("voteSum"),item.get("voteCount"),item.get("voteUrl"),item.get("viewUsersUserReviewsUrl"),item.get("customerType"),cc]
			c.execute('INSERT INTO Uber VALUES (' + ','.join("?" * len(payloads)) + ') ' , payloads)
			conn.commit()	
		start += 100
		end += 100
		time.sleep(1)
	except Exception as e:
  		print (e,",sleep 10s",end="")
  		time.sleep(10)

#print (json.dumps(data, indent=4,ensure_ascii=False))#json.dump default use ascii

'''
       {
        
        "rating": 5,
		"name": "点丫丫1314",
        "userReviewId": "1350942245",
        "title": "很方便，"
        "body": "上次在成都被那个恶心的师傅故意转路，投诉了过后把差价补给我了。。。还是非常不错。",
        "date": "2016-03-20T23:13:00Z",
        
		"voteSum": 0,
        "voteCount": 0,
        "voteUrl": "https://userpub.itunes.apple.com/WebObjects/MZUserPublishing.woa/wa/rateUserReview?userReviewId=1350942245",
        "viewUsersUserReviewsUrl": "https://itunes.apple.com/cn/reviews?userProfileId=449009503",
        "customerType": "Customers"
        
        
        },
'''



