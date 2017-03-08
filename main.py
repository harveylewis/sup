import atc, userdata, pause, requests
from time import sleep
from utils import *
from pushbullet import Pushbullet



pb = Pushbullet(userdata.api_key)


with requests.Session() as session:
	session.headers.update(
		{
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
	})


def wait_for_update(time_to_start, previous_data): ## Used to wait for new products to be added
#Time_to_start in epoch time format

	pause.until(time_to_start)
	while True:
		sleep(0.5)
		print GMT() + ' :: Parsed for new links'
		req = session.get(HOME_URL)
		data = req2.json()

		if data != previous_data:
			break
	
	return data


def find_best_matched(keywords, category, data):

	item_names = [] ## initialise lists
	item_ids = []

	if category != 'new':
		category = category.title()

	for item in data['products_and_categories'][category]: ##Item category here
		item_names.append(item['name'])
		item_ids.append(item['id'])

	##Zip both to dictionary
	item_dictionary = dict(zip(item_names, item_ids))


	
	matches_dict={}

	for item in item_names:
		matches=0
		low_item = item.lower()
		for word in keywords:
			low_word = word.lower()
			if low_word in low_item:
				matches=matches+1

		matches_dict[item] = matches


	best_match = max(matches_dict, key=matches_dict.get)
	item_id = str(item_dictionary[best_match])

	return best_match, item_id


def find_size_id(page_data):

	if userdata.ACCESSORY:
		for section in page_data['styles']:
			for size in section['sizes']:
				return size['id']

	else:
		for target in userdata.COLOUR:
			for colourway in page_data['styles']:
				if target in colourway['name']:
					for size in colourway['sizes']:

						if userdata.ONE_SIZE:
							return size['id']

						else:
							if userdata.SIZE == size['name']:
								return size['id']

def find_style_id(page_data):


	if userdata.ACCESSORY:
		for colourway in page_data['styles']:
			return colourway['id']

	else:
		for target in userdata.COLOUR:
			for colourway in page_data['styles']:
				if target.lower() in colourway['name'].lower():
					return colourway['id']


def get_item_info(item_id): ##Get all data for checking out

	product_page_data = session.get('http://www.supremenewyork.com/shop/{}.json'.format(item_id)).json()
	size_id = find_size_id(product_page_data)
	style_id = find_style_id(product_page_data)
	return size_id, style_id




'''
MAIN CODE
'''

print x_('USER DETAILS')
print grey_(GMT() + lb_('Your keywords are: ' + userdata.keywords_string))
print grey_(GMT() + lb_('The target size is: ' + userdata.SIZE))
print grey_(GMT() + lb_('The target colour is: ' + userdata.colour_string))
print grey_(GMT() + lb_('Ghost delay is: ' + str(userdata.DELAY) + ' seconds'))
print grey_(GMT() + lb_('Waiting until 10:59 before starting script'))
print
print

request = session.get('http://www.supremenewyork.com/mobile_stock.json')
data = request.json()


print x_('SCRIPT STARTED')
new_data = wait_for_update(1489057185, data)
item_name, item_id = find_best_matched(userdata.KEYWORDS, userdata.CATEGORY, new_data)
size_id, style_id = get_item_info(item_id)


atc.add_to_cart(size_id, item_id, style_id)
sleep(userdata.DELAY)
checkout = atc.checkout(item_name, size_id)



