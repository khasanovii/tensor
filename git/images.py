import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from browser import browser, get_page
from function import find, click, send, wait, attribute, check, check_empty, switch_tab, current_url

class_names = list()
class_names = [
	'modal__close',
	'services-new__content',
	'services-new__item-title',
	'PopularRequestList-Item_pos_0',
	'PopularRequestList-SearchText',
	'input__box',
	'serp-item_pos_0',
	'serp-item__link',
	'ImagesViewer-Container',
	'MediaViewer-ButtonNext',
	'MediaViewer-ButtonPrev'
]
# create a new Firefox session
url= 'https://www.yandex.ru/'
browser = browser()
driver = get_page(url, browser)
modal_close = find(driver,'class',class_names[0])
# closing modal window
# wait time for loading data
wait(15)
click(driver, modal_close)
# end closing modal window
# search service content
services = find(driver, 'class', class_names[1])
# search images service
a = find(services,'selector','a[data-id="images"]')
# get name service
images = find(a,'class',class_names[2])
# check service name with before define name
button_text = attribute(images,'innerHTML')
text = 'Картинки'
check(button_text, text, 'Images link was found on this page','Images link was not found on this page')
# open page this service
click(driver,a)
wait(10)
# wait loading
wait(10)
# switch to new tab 
switch_tab(driver,1)
# get url current page
url_current_page = current_url(driver)
# check url with before define url
# select first images catalog
first_catalog = find(driver,'class',class_names[3])
# get link
a_image_catalog = find(first_catalog,'tag','a')
# get name images catalog
catalog = find(first_catalog,'class',class_names[4])
catalog_name = attribute(catalog,'innerHTML')
# open first images catalog
click(driver,a_image_catalog)
# search input field
input_box = find(driver,'class',class_names[5])
input = find(input_box,'tag','input')
input_value = attribute(input,'value')
# check select catalog name and value in input
check(input_value,catalog_name,"The names match","The names don't match")
# search first image
wait(5)
first_image = find(driver,'class',class_names[6])
# search link first image
a = find(first_image,'class',class_names[7])
# open first image
click(driver,a)
# check opened images slider
slider = find(driver,'class',class_names[8])
# get link image
opened_image = find(slider,'tag','img')
opened_image_url = attribute(opened_image,"src")
# search button next image
button_next = find(driver,'class',class_names[9])
click(driver,button_next)
# search button previous image
button_previous = find(driver,'class',class_names[10])
# search next image
next_image = find(slider,'tag','img')
next_image_url = attribute(next_image,"src")
#print(next_image_url)
click(driver,button_previous)
previous_image = find(slider,'tag','img')
previous_image_url = attribute(previous_image,'src')
# check url images
check(previous_image_url,opened_image_url,"Image url previous match: ","Image url previous not match")