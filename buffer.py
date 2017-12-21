## Algorithm Buffer overflow attack.
print "Buffer Overflow"
print "Enter Choice"
print "1 . See Buffer overlow Violation"
print "2 . See smooth buffer overflow handling"

ch = int(raw_input("Enter - > "))


if ch == 1 :
	buffer=[None]*10
	for i in range(0,14):
		data = raw_input("Enter the value for position : " )
		buffer[i]=data
		print buffer[i]
else :
	try:
		buffer=[None]*10
		for i in range(0,14):
			buffer[i]=7
	except Exception as e: 
		print "Error Generated => " + str(e)