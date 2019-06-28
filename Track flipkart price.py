import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
import time

def check_price():
		URL = "https://www.flipkart.com/optimum-nutrition-gold-standard-100-whey-protein/p/itmeavtn8uhzgxez?pid=PSLEAVTNUGYWHRCZ&lid=LSTPSLEAVTNUGYWHRCZUMIX9W&marketplace=FLIPKART&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=881438ca-26e9-42f7-a512-52d6733ef68e.PSLEAVTNUGYWHRCZ.SEARCH&ppt=sp&ppn=sp&ssid=gulco9wm2o0000001561697716715&qH=e385ce1fca93bc49"
		headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

		page = requests.get(URL,headers=headers)
		soup = BeautifulSoup(page.content,'html.parser')

		title = soup.find('span', {"class": "_35KyD6"}).get_text()
		price = soup.find('div', {"class": "_2i1QSc"}).get_text()
		price = int(price[1:2]+price[3:6])
		if(price<3000):
			send_mail(title)
		print(title)
		print(price)

def send_mail(title):
		server = smtplib.SMTP('smtp.gmail.com',587)
		server.ehlo() #It's a command that authenticate connection with gmail server.
		server.starttls() #It's a command that start our connection with gamil server connection.
		server.ehlo()

		server.login("darshak.patidar7@gmail.com","darshak@78")

		subject = "Hey,Price Fall Down of :"+title
		body = 'check flipkart link: https://www.flipkart.com/optimum-nutrition-gold-standard-100-whey-protein/p/itmeavtn8uhzgxez?pid=PSLEAVTNUGYWHRCZ&lid=LSTPSLEAVTNUGYWHRCZUMIX9W&marketplace=FLIPKART&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=881438ca-26e9-42f7-a512-52d6733ef68e.PSLEAVTNUGYWHRCZ.SEARCH&ppt=sp&ppn=sp&ssid=gulco9wm2o0000001561697716715&qH=e385ce1fca93bc49'
	    

		msg=EmailMessage()
		msg['Subject'] = subject
		msg['From'] = "darshak.patidar7@gmail.com"
		msg['To'] = 'darshak.ranpariya@gmail.com'
		msg.set_content(body)
		server.send_message(msg)
		print("Email sended")
		server.quit()

while 1:
	check_price()
	time.sleep(60*60)

