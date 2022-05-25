import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def find(driver, attribute, data) : 
	if(attribute == 'class') : 
		element = driver.find_element(By.CLASS_NAME, data)
	elif(attribute == 'tag') : 
		element = driver.find_element(By.TAG_NAME, data)
	elif(attribute == 'selector') : 
		element = driver.find_element(By.CSS_SELECTOR, data)
	return element	
def click(driver, target) : 
	webdriver.ActionChains(driver).click(target).perform()
def send(driver, key) : 
	driver.send_keys(key)
def wait(seconds) : 
	time.sleep(seconds)
def attribute(element, data) : 
	return	element.get_attribute(data)
def check(a,b,text1,text2) : 
	if(a == b) : 
		print(text1,a) 
	else :
		print(text2)
def check_empty(a,text1,text2) : 
	if(a != '') : 
		print(text1)
	else : 
		print(text2)