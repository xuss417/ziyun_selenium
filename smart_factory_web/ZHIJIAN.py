# coding:utf-8
import sys

import random
import requests
import json
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("https://iot.qa.ziyun-cloud.net/manufacture/login.html")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("ZY000217315161")
#driver.find_element_by_id("username").send_keys(Keys.NUMPAD2)

time.sleep(2)
driver.find_element_by_id("pwd").clear()
driver.find_element_by_id("pwd").send_keys("P1234")
time.sleep(2)
driver.find_element_by_id('sub_btn').click()
time.sleep(1)
action = ActionChains(driver)
#接收
driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[3]/a/span').click()
time.sleep(1)

time.sleep(2)
ele = driver.find_element_by_xpath('/html/body/div[2]/div')
action.move_to_element(ele).click().send_keys('1529').perform()
#driver.find_element_by_xpath('/html/body/div[2]/div').send_keys(Keys.CONTROL,"1529")
time.sleep(2)
driver.find_element_by_id('submit_btn').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[4]/a/i').click()
time.sleep(5)
'''
#设备绑定
ele2 = driver.find_element_by_xpath('/html/body/div[2]/div[1]')
action.move_to_element(ele2).send_keys('201').perform()
#批次绑定
time.sleep(10)

'''
ele3 = driver.find_element_by_xpath('/html/body/div[2]/div[2]')
ele3.send_keys('1529')
#action.move_to_element(ele3).click().send_keys('1529').perform()
time.sleep(2)
#普通质检
driver.find_element_by_xpath('//*[@id="skip_tip"]/div/div[2]/a[1]').click()
deliver_num = driver.find_element_by_id('deliver_num').text
print(deliver_num -1)
js1 = driver.find_element_by_xpath('html/body/div[2]')
driver.execute_script("arguments[0].scrollIntoView();",js1)
time.sleep(2)
driver.find_element_by_id('excellent_input').clear()
time.sleep(2)
driver.find_element_by_id('excellent_input').send_keys(deliver_num)
time.sleep(2)
driver.find_element_by_id('submit_btn').click()

#特殊质检
'''driver.find_element_by_xpath('.//*[@id="skip_tip"]/div/div[2]/a[2]').click()

time.sleep(2)'''

#交付
driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[2]/a/span').click()
time.sleep(2)
ele4 = driver.find_element_by_xpath('//*[@id="scan_div"]/div')
#action.move_to_element(ele4).click().send_keys('1529').perform()
ele4.send_keys('1529')
time.sleep(5)
'''#一次交付
driver.find_element_by_xpath('html/body/div[4]/div[3]/div[1]/ul/li[2]/a/i').click()
time.sleep(2)
driver.find_element_by_id('exceptional_add_btn').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="exceptional_container"]/span/input').clear()
driver.find_element_by_xpath('//*[@id="exceptional_container"]/span/input').send_keys('ABB01')'''
'''js = driver.find_element_by_xpath('html/body/div[4]')
js_scroll = 'document.getElementsByClassName("scroll")[0].scrollTop=10000'
driver.execute_script("arguments[0].scrollIntoView();",js)
'''
driver.find_element_by_xpath('//*[@id="submit_btn"]').click()
time.sleep(1)
