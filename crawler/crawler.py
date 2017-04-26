# coding=utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup

#	判斷整數
def upbound_int(upbound):
	
	# value 	待判斷之值
	# upbound	value之上限
	print()
	while 1:
		value = input()
		if(value.isnumeric() and isinstance(int(value),int) and int(value) > -1 and int(value)<upbound):
			value = int(value)
			return value
		print('re-enter')


types = ['\"Customize\"',"NEWS"]

visit_webs = ['']
visit_webs.append("http://www.chinatimes.com/")

for i in range(0,len(types),1):
	print(i,"\t",types[i])

s_web = upbound_int(len(visit_webs))

if(s_web == 0):
	visit_webs[0] = input('Give the webs that you want to crawler:\n')

print()

#送出GET請求到遠端伺服器，伺服器接受請求後回傳<Response [200]>，代表請求成功
res = urlopen(visit_webs[int(s_web)])
soup = BeautifulSoup(res,'html.parser')

#印出網頁內容
#print(soup)
 
contents = [];
contents.append('\"Customize"')
contents.append('h1')
contents.append('h2')
contents.append('a')
contents.append('li')

#重複爬

while 1:

	#爬蟲內容
	print("Crawler Title:")
	for i in range(0,len(contents),1):
		print(i,"\t",contents[i])

	s_content = upbound_int(len(contents))

	if(s_content == 0):
		contents[0] = input()

	#使用select選取特定元素
	title = soup.select(contents[s_content])

	#印出標題及內文
	print()
	for i in range(0,len(title),1):
		print()
		print(i,'\t',title[i].get_text().strip())
	
	print()
	
	#是否繼續爬蟲
	b_con = input("Continue crawler / Not (1-Continue)\n")

	if(not b_con == '1'):
		break