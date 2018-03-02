#coding:utf-8
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
driver.find_element_by_id("username").send_keys("ZY000218215161")
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
time.sleep(2)
#设备绑定
ele2 = driver.find_element_by_xpath('/html/body/div[2]/div[1]')
action.move_to_element(ele2).send_keys('201').perform()
#批次绑定
time.sleep(10)
ele3 = driver.find_element_by_xpath('/html/body/div[2]/div[2]')
#action.move_to_element(ele3).send_keys('1529').perform()
ele3.send_keys('1529')
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div[5]/a').click()
time.sleep(2)

#交付
driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[2]/a/span').click()
time.sleep(2)
ele4 = driver.find_element_by_xpath('//*[@id="scan_div"]/div')
ele4.send_keys('1529')
#action.move_to_element(ele4).click().send_keys('1529').perform()
time.sleep(2)
driver.find_element_by_id('submit_btn').click()
time.sleep(1)
