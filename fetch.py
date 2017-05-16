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
	'''Logging Fuction'''
	ts=time.asctime()
	print('[',ts,']',end='')
	sys.stdout.writelines(dt)
	print()
	sys.stdout.flush()
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
			fout=open(getpath(),'w+')
			try:
				text=rem.read()
				text=text.decode('UTF-8')
				text=text.split('\n')
				del text[0],text[-1]
				text=[line+'\n' for line in text]
				fout.writelines(text)
			except Exception as e:
				logger('Error:',e)
			fout.close()
			logger('TXT update done. Now sleep.')
		time.sleep(1800)
