import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from browser import browser, get_page
from function import find, click, send, wait, attribute, check, check_empty

url = 'https://www.yandex.ru/'
browser = browser()
driver = get_page(url, browser)
# closing modal window
modal_close = find(driver,'class','modal__close')
# wait time for loading data
wait(15)
click(driver, modal_close)
# end closing modal window
# begin search input for search information
input = find(driver,'class', 'input__input')
# input word for search
send(input,'тензор')
# search suggest table
wait(5)
suggest = find(driver,'class','mini-suggest__popup_visible')
# check visible or hidden suggest table
check_empty(suggest,'suggest visible','suggest not visible')
# press enter button on keyboard for begin search
send(input,Keys.ENTER)
# after opening begin search first link, first we find content table with result url 
wait(2)
content_left = find(driver,'class','content__left')
# get list ul
ul = find(content_left,'tag','ul')
# get list element li with data-attribute
li= find(ul,'selector','li[data-cid="0"]')
# get link a
a = find(li,'tag','a')
# get href for check url 
url = attribute(a,"href")
# check url
url_check = 'https://tensor.ru/'
check(url,url_check,'First link : ', 'Another link')