'''
Module to Add to cart and checkout supreme
'''
import userdata
from utils import *
import requests
from pushbullet import Pushbullet



notifications = userdata.notifications_on
pb = Pushbullet('o.noQTZAyXTgibHUJTycFvbcOvLXnWrqtu')
session = requests.Session()

def add_to_cart(sizeid, item_id, style_id):

	atc_url = ('http://www.supremenewyork.com/shop/{}/add.json').format(item_id)


	cart_headers={
			'Host': 'www.supremenewyork.com',
			'Accept': 'application/json',
			'Proxy-Connection': 'keep-alive',
			'X-Requested-With': 'XMLHttpRequest',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'en-us',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Origin': 'http://www.supremenewyork.com',
			'Connection': 'keep-alive',
			'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D257',
			'Referer': 'http://www.supremenewyork.com/mobile'
		}

	payload ={
	'qty' : '1',
	'size':(sizeid),
	'style':(style_id)
		}

	print grey_((GMT() + lb_('Sending add to cart request')))

	add_response = session.post(atc_url, headers=cart_headers, data=payload)

	if add_response.status_code!=200:
		print grey_(GMT() + r_(add_response.status_code,'Error' '\n            Did not add to cart'))
		print


	else:
		print grey_(GMT() + g_('Successfully added to cart'))
		print



def checkout(item_name, size_id):
	checkout_payload={
	'from_mobile':'1',
	'cookie-sub': '%7B%22'+str(size_id)+'%22%3A1%7D',
	'order[billing_name]':userdata.user_full_name,
	'order[email]':userdata.user_email,
	'order[tel]':userdata.user_tel,
	'order[billing_address]':userdata.user_address_line1,
	'order[billing_address_2]':userdata.user_address_line2,
	'order[billing_address_3]':userdata.user_address_line3,
	'order[billing_city]':userdata.user_city,
	'order[billing_zip]':userdata.user_zip,
	'order[billing_country]':'GB', #change for country
	'same_as_billing_address':'1',
	'store_credit_id':'',
	'credit_card[type]':'visa',  #change for card type
	'credit_card[cnb]':userdata.user_cc_number,
	'credit_card[month]':userdata.user_cc_expiry_month,
	'credit_card[year]':userdata.user_cc_expiry_year,
	'credit_card[vval]':userdata.user_cc_security_code,
	'order[terms]':'0',
	'order[terms]':'1',   #don't change
	'hpcvv':'',
	'commit':'process payment'
	}

	checkout_headers={
	'Host': 'www.supremenewyork.com',
	'Accept': 'application/json',
	'Proxy-Connection': 'keep-alive',
	'X-Requested-With': 'XMLHttpRequest',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'en-us',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Origin': 'http://www.supremenewyork.com',
	'Connection': 'keep-alive',
	'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D257',
	'Referer': 'http://www.supremenewyork.com/mobile/#checkout'
	}
	
	print grey_(GMT() + lb_('Sending checkout request'))
	checkout_url = 'https://www.supremenewyork.com/checkout.json'
	response = session.post(checkout_url, headers=checkout_headers, data=checkout_payload)



	if response.status_code!=200:
		print grey_(GMT() + r_('Checkout failed'))
		print grey_(GMT() + r_('Did not checkout'))
		print
		if notifications:
	   		pb.push_note('Did not checkout', 'Did not get successful response on checkout request')

		return False



	elif response.status_code ==200:
		if 'outofstock' in response.text.lower():
			print grey_(GMT() + r_('Checkout failed'))
			print grey_(GMT() + r_('Item out of stock'))
			print
			if notifications:
	   			pb.push_note('Did not checkout', 'Item out of stock')
			return False


		elif 'failed' in response.text.lower():
			print grey_(GMT() + r_('Checkout failed'))
			print grey_(GMT() + r_('User data incorrect'))
			print
			if notifications:
	   			pb.push_note('Did not checkout', 'User data incorrect')
			return False


		else:
			print (grey_(GMT())) + g_('Successfully checked out')
			print
			if notifications:
				pb.push_note(item_name + ' checked out', 'Response 200 on checkout request, Check for confirmation email')

			return True

