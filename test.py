#!/usr/bin/env python
#-*-coding:UTF-8-*-
import re
import urllib2,models


for n in range(2000,18000):
	url = "http://model.kdslife.com/show/photo/%d.html"%n
	http = urllib2.urlopen(url)
	try:
		imgurl = re.search("(href.*?imgsrc=)(http://model\.img\..*?)(\">)",http.read()).group(2)
	except Exception, e:
		print url,"failed"
		continue
	finally:
		http.close()

	try:
		p = models.Picture().create(index=n,img_url=imgurl)
	except Exception,e:
		pass


	print n


 
	

