import time
import urllib.request
import sys
def decodefiletolist(enc,coder='UTF-8'):
	enc=enc.decode(coder)
	enc=enc.split('\n')
	del enc[0],enc[-1]
	enc=[line+'\n' for line in enc]
	return enc

def spam(strlist):
	if '<head>' in strlist:
		return None
	else:
		return strlist

def getpath():
	conf=open('today.config','r')
	st=conf.read()
	key,pt=st.split('=')
	if key=='path':
		return pt

def debug(b):
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


#Main Function starts here.
if __name__ == '__main__':
	debug(False)
	while True:
		#Fetch Remote file from the server.
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
				text=spam(decodefiletolist(rem.read()))
				fout.writelines(text)
			except Exception as e:
				logger('Error:',e)
			fout.close()
			logger('TXT update done. Now sleep.')
		time.sleep(1800)
