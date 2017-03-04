import os, ConfigParser, json
from pushbullet import Pushbullet


PROJECT_ROOT_DIR = os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir)))
c = ConfigParser.ConfigParser()
configFilePath = os.path.join(PROJECT_ROOT_DIR + '/github', 'supconfig.cfg')
c.read(configFilePath)


KEYWORDS = (json.loads(c.get("Item1","KEYWORDS")))
keywords_string = ', '.join(KEYWORDS)

COLOUR = (json.loads(c.get("Item1","COLOUR")))
colour_string = ', '.join(COLOUR)

CATEGORY = c.get("Item1","CATEGORY")

SIZE = c.get("Item1","SIZE")
ONE_SIZE = c.getboolean("Item1","ONE_SIZE")
ACCESSORY = c.getboolean("Item1","Accessory")
DELAY = (int(c.get("Preferences","ghost_delay")))


user_full_name=c.get("User","user_full_name")
user_email= c.get("User","user_email")
user_tel= c.get("User","user_tel")
user_address_line1= c.get("User","user_address_line1")
user_address_line2= c.get("User","user_address_line2")
user_address_line3= c.get("User","user_address_line3")
user_city= c.get("User","user_city")
user_zip= c.get("User","user_zip") 
user_cc_number= c.get("User","user_cc_number")
user_cc_expiry_month= c.get("User","user_cc_expiry_month")
user_cc_expiry_year= c.get("User","user_cc_expiry_year")
user_cc_security_code= c.get("User","user_cc_security_code")

notifications_on = c.getboolean("Notifications", "notifications_on")
api_key = c.get("Notifications", "api_key")

if notifications_on:
	api_key = c.get("Notifications", "api_key")
	pb = Pushbullet(api_key)