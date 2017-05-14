import time
import urllib.request
def getpath():
	conf=open('today.config','r')
	st=conf.read()
	key,pt=st.split('=')
	if key=='path':
		return pt
if __name__ == '__main__':
	try:
		flag=True
		rem=urllib.request.urlopen('http://www.ipip5.com/today/api.php?type=txt')
		if rem.getcode()!=200:
			flag=False
	except Exception as e:
		flag=False
		print('An error occured:',e)

	if flag==True:
		fout=open(getpath(),'wb+')
		try:
			text=rem.read()
			fout.write(text)
		except Exception as e:
			print('An error occured:',e)
		fout.close()

	time.sleep(1800)
