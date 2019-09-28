
import requests
from bs4 import BeautifulSoup
import smtplib


URL = 'https://www.amazon.com/Apple-MQGJ2AM-A-Lightning-USB-C/dp/B07CMN7DCX/ref=sr_1_3?crid=2BI43GKWSHWQL&keywords=usbc+to+lightning&qid=1568829787&sprefix=usbc+to+lig%2Caps%2C125&sr=8-3'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

def check_price():

	page = requests.get(URL, headers = headers)

	soup = BeautifulSoup(page.content,'html.parser')

	title = soup.find(id="productTitle").get_text()

	price = soup.find(id="priceblock_ourprice").get_text()
	print(title.strip())
	convertedPrice = float(price.replace("$",""))
	
	# if(convertedPrice < 20.00):
		send_mail()
	print(convertedPrice)
	print(title.strip())

def send_mail():
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('luismoran2010@gmail.com', 'rjtipmccpnwrwubx')
	subject = "Price Fell"
	body = "Check Amazon link \n https://www.amazon.com/Apple-MQGJ2AM-A-Lightning-USB-C/dp/B07CMN7DCX/ref=sr_1_3?crid=2BI43GKWSHWQL&keywords=usbc+to+lightning&qid=1568829787&sprefix=usbc+to+lig%2Caps%2C125&sr=8-3"

	msg = f"subject: {subject}\n\n{body}"

	server.sendmail(
		'luismoran2010@gmail.com',
		'luismoran2010@gmail.com',
		msg
		)
	print("Hey email has been sent")

	server.quit()

check_price()




# convertedPrice = 