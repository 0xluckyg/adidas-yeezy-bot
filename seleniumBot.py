from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui

import requests
import bs4
import random
import webbrowser
import threading
import time

MODEL = 'S82241'
FIRSTNAME = 'SCOTT'
LASTNAME = 'CHO'
ADDRESS = 'Some Address'
APTNUM = 'Some Apt Number'
ZIPCODE = 'Some Zip Number'
CITY = 'Some City'
CARDNUM = '1234567890'
CARDNAME = 'Name on Card'
PHONENUM = '123456789'
EMAIL = 'email@email.com'
SECURITYCODE = '123'


baseURL = 'http://www.adidas.com/us/' + MODEL + '.html?'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

driver = webdriver.Chrome()
driver.get(baseURL)

sizeSelect = WebDriverWait(driver, 1000000).until(
EC.element_to_be_clickable((By.XPATH, '//*[@id="buy-block"]/div[1]/div[5]/div[3]/form/div[2]/div[2]')));
sizeSelect.click()
size = driver.find_element_by_xpath('//*[@id="buy-block"]/div[1]/div[5]/div[3]/form/div[2]/div[2]/div/div/div/div[2]/div/ul/li[7]')
size.click()

time.sleep(0.3)
cart = driver.find_element_by_name('add-to-cart-button')
cart.click()

checkout = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.CLASS_NAME, "btn_checkout")));
checkout.click();

# time.sleep(0.5)
# checkout = driver.find_element_by_class_name('btn_checkout')
# checkout.click()

# time.sleep(1)
firstName = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.ID, 'dwfrm_delivery_singleshipping_shippingAddress_addressFields_firstName')));
firstName.send_keys(FIRSTNAME)

lastName = driver.find_element_by_id('dwfrm_delivery_singleshipping_shippingAddress_addressFields_lastName')
lastName.send_keys(LASTNAME)

streestAddress = driver.find_element_by_id('dwfrm_delivery_singleshipping_shippingAddress_addressFields_address1')
streestAddress.send_keys(ADDRESS)

appartment = driver.find_element_by_id('dwfrm_delivery_singleshipping_shippingAddress_addressFields_address2')
appartment.send_keys(APTNUM)

city = driver.find_element_by_id('dwfrm_delivery_singleshipping_shippingAddress_addressFields_city')
city.send_keys(CITY)

stateSelect = driver.find_element_by_xpath('//*[@id="dwfrm_delivery"]/div[2]/div[2]/div/fieldset/div/div[1]/div[6]/div[1]')
stateSelect.click()
ActionChains(driver).send_keys('n').perform()
state = driver.find_element_by_xpath('//*[@id="dwfrm_delivery"]/div[2]/div[2]/div/fieldset/div/div[1]/div[6]/div[1]/div/div/div/div[2]/div/ul/li[37]');
state.click()

zipCode = driver.find_element_by_id('dwfrm_delivery_singleshipping_shippingAddress_addressFields_zip')
zipCode.send_keys(ZIPCODE)

phone = driver.find_element_by_id('dwfrm_delivery_singleshipping_shippingAddress_addressFields_phone')
phone.send_keys(PHONENUM)

email = driver.find_element_by_id('dwfrm_delivery_singleshipping_shippingAddress_email_emailAddress')
email.send_keys(EMAIL)

cashOut = driver.find_element_by_xpath('//*[@id="dwfrm_delivery_savedelivery"]')
cashOut.click()

# time.sleep(1)
cardName = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.ID, 'dwfrm_payment_creditCard_owner')));
cardName.clear()
cardName.send_keys(CARDNAME)

cardNumber = driver.find_element_by_id('dwfrm_payment_creditCard_number')
cardNumber.send_keys(CARDNUM)

cardMonthList = driver.find_element_by_xpath('//*[@id="dwfrm_payment"]/fieldset/div/div[4]/div[2]/div/div')
cardMonthList.click()
#Jan = 2 Feb = 3 Mar = 4...
cardMonth = driver.find_element_by_xpath('//*[@id="dwfrm_payment"]/fieldset/div/div[4]/div[2]/div/div/div/div/div[2]/div/ul/li[2]')
cardMonth.click()

cardYearList = driver.find_element_by_xpath('//*[@id="dwfrm_payment"]/fieldset/div/div[4]/div[3]/div[1]/div')
cardYearList.click()
#2019 = 4 2020 = 5 2021 = 6...
cardYear = driver.find_element_by_xpath('//*[@id="dwfrm_payment"]/fieldset/div/div[4]/div[3]/div[1]/div/div/div/div[2]/div/ul/li[5]')
cardYear.click()

securityCode = driver.find_element_by_id('dwfrm_payment_creditCard_cvn')
securityCode.send_keys(SECURITYCODE)

BUY = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[4]/div/button')
BUY.click()

# driver.quit()
