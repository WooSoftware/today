import time
import urllib.request
import sys
def getpath():
	conf=open('today.config','r')
	st=conf.read()
	key,pt=st.split('=')
	if key=='path':
		return pt

def usestd(b):
	if b==False:
		lout=open('log','w+')
		sys.stdout=lout

def logger(*dt):
	ts=time.asctime()
	print('[',ts,']',dt)
if __name__ == '__main__':
	usestd(False)
	while True:
		try:
			flag=True
			rem=urllib.request.urlopen('http://www.ipip5.com/today/api.php?type=txt')
			if rem.getcode()!=200:
				flag=False
		except Exception as e:
			logger('Error:',e)
			flag=False
				
		if flag==True:
			logger('TXT fetch success')
			fout=open('D:\\today.txt,'wb+')
			try:
				text=rem.read()
				fout.write(text)
			except Exception as e:
				logger('Error:',e)
			fout.close()
			logger('TXT update done')
		time.sleep(1800)
