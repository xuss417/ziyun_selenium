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
from selenium.webdriver.support.select import Select


def select_by_text(self, locator,index):
    element = self.find_element(locator)
    Select(element).select_by_index(index)

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
#异常接收
driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[3]/a/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div').send_keys("1744")
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[1]/ul/li[2]/a/i').click()
driver.find_element_by_xpath('/html/body/div[3]/div[2]/ul/li[3]/strong/div/div/div[1]').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[3]/div[2]/ul/li[3]/strong/div/div/div[2]/ul/li[1]').click()
time.sleep(2)
driver.find_element_by_id('submit_btn').click()
time.sleep(1)