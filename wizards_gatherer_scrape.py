import tkinter
import sys
from urllib.request import urlopen
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import csv
import time
import re


def getBs(url):
	try:
		user_agent = 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
		req = urllib.request.Request(url, None, {'User-Agent' : user_agent})
		html = urllib.request.urlopen(req)
		
		#req = urllib.request.Request(url, data, headers)
		#with urllib.request.urlopen(req) as response:
		#   html = response.read()
	except Exception as e:
		print(e)
		return None
	else:
		if html is None:
			print("URL is not found")
			return None
	
	bsObj = BeautifulSoup(html, "html.parser");
	
	return bsObj

pageNum = 0
entries = ""
first = ''

table = getBs(sys.argv[1]+"&page="+str(pageNum)).find_all('span', attrs={'class':'cardTitle'})

while len(table) != 0:
	if first == table[0]:
		break
	else: 
		first = table[0]
	
	for row in table:
		entries+="1x " + row.a.string+ "\n";
		prev = row.a.string
	
	pageNum+=1
	print("going to page" + str(pageNum))
	table = getBs(sys.argv[1]+"&page="+str(pageNum)).find_all('span', attrs={'class':'cardTitle'})

if pageNum==0:
	print("ERROR: No results retured")
else:
	print("ok to paste. 5 seconds")
	
root = tkinter.Tk()
root.withdraw()
root.clipboard_clear()
root.clipboard_append(entries)
root.after(2000, root.destroy)
root.mainloop()
	