print "Buffer Overflow"
print "Enter Choice"
print "1 . See Buffer overlow Violation"
print "2 . See smooth buffer overflow handling"

ch = int(raw_input("Enter - > "))


if ch == 1 :
	buffer=[None]*10
	for i in range(0,14):
		buffer[i]=7
else :
	try:
		buffer=[None]*10
		for i in range(0,14):
			buffer[i]=7
	except Exception as e: 
		print "Error Generated => " + str(e)
	
	
