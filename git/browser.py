from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# create a new FireFox session
def browser() : 
	browser = webdriver.Firefox()
	return browser
def get_page(url,driver) : 
	#browser()
	driver.get(url)
	return driver