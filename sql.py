#encoding=utf-8
import sqlite3
import jieba
import jieba.analyse
def count(all_rows):
	arr = [0,0,0,0,0]
	for entry in all_rows:
		arr[entry[0]-1] += 1
	return arr

conn = sqlite3.connect('uber.sqlite')
c = conn.cursor()
c.execute('select rating,body from Uber WHERE cc="cn"')
all_rows = c.fetchall()

#Set big dictionary
jieba.set_dictionary('util/dict.txt.big')

arr = count(all_rows)
content=["","","","",""]
for entry in all_rows:
	content[entry[0]-1] += entry[1]+","
for idx,c in enumerate(content):
	#tags = jieba.analyse.extract_tags(c, 100, withWeight=True)
	print ("\n",idx+1,"Score Rating:", arr[idx])
	#print (tags)
	for x, w in jieba.analyse.extract_tags(c,30, withWeight=True):
		print('%s %s' % (x, round(w,3)),end="  /")
	#print("/ ".join(seg_list))
#print (count(all_rows))





