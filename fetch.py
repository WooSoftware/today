import time
import urllib.request
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
		fout=open('today.txt','wb+')
		try:
			text=rem.read()
			fout.write(text)
		except Exception as e:
			print('An error occured:',e)
		fout.close()

	time.sleep(1800)
