from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import ConfigParser

def setup(configfile):
	config=ConfigParser.ConfigParser()
	config.read(configfile)
	return config
	
def login_to_fb(configfile):
	config=setup(configfile)
	usr = config.get("User","username")
	pwd = config.get("User","password")
	firefox_profile = webdriver.FirefoxProfile()
	firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
	driver = webdriver.Firefox(firefox_profile=firefox_profile)
	# or you can use Chrome(executable_path="/usr/bin/chromedriver")
	driver.get("http://www.facebook.org")
	assert "Facebook" in driver.title
	elem = driver.find_element_by_id("email")
	elem.send_keys(usr)
	elem = driver.find_element_by_id("pass")
	elem.send_keys(pwd)
	elem.send_keys(Keys.RETURN)
	return driver

#elem = driver.find_element_by_css_selector(".input.textInput")
#elem.send_keys("Posted using Python's Selenium WebDriver bindings!")
#elem = driver.find_element_by_css_selector("input[value=\"Publicar\"]")
#elem.click()



#driver.close()

