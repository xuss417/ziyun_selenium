#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
driver = webdriver.Firefox()
driver.get("https://iot.qa.ziyun-cloud.net/new_factory/login.html")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_id("userName").clear()
driver.find_element_by_id("userName").send_keys("ZY000217715161")
time.sleep(2)
driver.find_element_by_id("pwd").clear()
driver.find_element_by_id("pwd").send_keys("P1234")
time.sleep(2)
code0 =driver.find_element_by_xpath('//*[@id="code0"]').text
code1 =driver.find_element_by_xpath('//*[@id="code1"]').text
code2 =driver.find_element_by_xpath('//*[@id="code2"]').text
code3 =driver.find_element_by_xpath('//*[@id="code3"]').text
allcode = code0+code1+code2+code3
print(allcode)

driver.find_element_by_id("code").clear()
driver.find_element_by_id("code").send_keys(allcode)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="checkLogin"]/div').click()
'''time.sleep(1)
driver.find_element_by_link_text('物料管理').click()
time.sleep(1)
driver.find_element_by_link_text('销售订单').click()'''
time.sleep(2)
driver.find_element_by_xpath('html/body/div[1]/aside/section/ul/li[4]/a/span').click()
time.sleep(2)
driver.find_element_by_xpath('html/body/div[1]/aside/section/ul/li[4]/ul/li[1]/a').click()
time.sleep(2)
#进入新增销售订单页面
#driver.find_element_by_link_text('新增销售订单').click()
driver.find_element_by_xpath('html/body/div[1]/div/section[2]/div[1]/span/a').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div/div/section[1]/ul/li[1]/div/input').clear()
driver.find_element_by_xpath('/html/body/div/div/section[1]/ul/li[1]/div/input').send_keys(str(random.randint(10,
                                                                                                              99999999)) + 'ABBC')
time.sleep(2)
driver.find_element_by_xpath('html/body/div[1]/div/section[1]/ul/li[2]/div/input').clear()
driver.find_element_by_xpath('html/body/div[1]/div/section[1]/ul/li[2]/div/input').send_keys('ABB')
time.sleep(2)
driver.execute_script('document.getElementById("end_time").removeAttribute("readonly");')
driver.find_element_by_id('end_time').clear()
driver.find_element_by_id('end_time').send_keys('2018-01-31 00:00:00')
driver.find_element_by_xpath('/html/body/div[1]/header/nav').click()
time.sleep(2)
driver.find_element_by_xpath('html/body/div[1]/div/section[2]/div[1]/div/span[1]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/section[2]/div[2]/div/div[1]/ul/li[1]/div/input').clear()
driver.find_element_by_xpath('/html/body/div[1]/div/section[2]/div[2]/div/div[1]/ul/li[1]/div/input').send_keys('加多宝很好喝')
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/section[2]/div[2]/div/div[1]/ul/li[2]/div/input').clear()
driver.find_element_by_xpath('/html/body/div[1]/div/section[2]/div[2]/div/div[1]/ul/li[2]/div/input').send_keys('100')
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/section[2]/div[2]/div/div[1]/ul/span[1]').click()
time.sleep(1)

#工艺员工操作部分
driver.get("https://iot.qa.ziyun-cloud.net/new_factory/login.html")
time.sleep(2)
driver.find_element_by_id("userName").clear()
driver.find_element_by_id("userName").send_keys("ZY000218015161")
time.sleep(2)
driver.find_element_by_id("pwd").clear()
driver.find_element_by_id("pwd").send_keys("P1234")
time.sleep(2)
code0 =driver.find_element_by_xpath('//*[@id="code0"]').text
code1 =driver.find_element_by_xpath('//*[@id="code1"]').text
code2 =driver.find_element_by_xpath('//*[@id="code2"]').text
code3 =driver.find_element_by_xpath('//*[@id="code3"]').text
allcode = code0+code1+code2+code3
print(allcode)
driver.find_element_by_id("code").clear()
driver.find_element_by_id("code").send_keys(allcode)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="checkLogin"]/div').click()
time.sleep(2)
driver.find_element_by_link_text('物料管理').click()
time.sleep(2)
driver.find_element_by_link_text('销售订单').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div/div/section[1]/ul[2]/p').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="remove_order_"]/div[5]/a[2]/i').click()
time.sleep(1)
#进入图纸编辑页面
#点击图纸上传
move_mouse = driver.find_element_by_xpath("/html/body/div[1]/div/section[2]/div[2]/div/div[1]/ul/span[4]/i")
ActionChains(driver).move_to_element(move_mouse).perform()
driver.find_element_by_xpath('/html/body/div[1]/header/nav').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/section[2]/div[2]/div/div[1]/ul/span[4]/i').click()
time.sleep(1)

driver.find_element_by_xpath('/html/body/div[1]/div/section[2]/div[2]/div/div[2]/div/div/ul[1]/li[1]/div/span/input').send_keys('C:\\Users\\dell\\Desktop\\img\\ABBtest.png')
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/section[2]/div[2]/div/div[2]/div/div/ul[1]/li[3]/div/input').clear()

driver.find_element_by_xpath('/html/body/div[1]/div/section[2]/div[2]/div/div[2]/div/div/ul[1]/li[3]/div/input').send_keys('100')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div/section[2]/div[2]/div/div[2]/div/div/ul[2]/li/div/a').click()
time.sleep(2)

proess_box_loc = driver.find_element_by_xpath('//*[@id="dragTag_wrapper"]/section[2]/div/div[1]/ul')
one_proess_loc = driver.find_element_by_xpath('//*[@id="Process_box"]/div/span[2]/em')
two_proess_loc = driver.find_element_by_xpath('//*[@id="Process_box"]/div/span[1]/em')
proesssure_loc = driver.find_element_by_xpath('//*[@id="dragTag_wrapper"]/section[2]/div/div[2]/a[1]')
ActionChains(driver).drag_and_drop(one_proess_loc,proess_box_loc,).perform()
time.sleep(2)
ActionChains(driver).drag_and_drop(two_proess_loc,proess_box_loc).perform()
time.sleep(2)
ActionChains(driver).drag_and_drop(one_proess_loc,proess_box_loc,).perform()
time.sleep(2)
ActionChains(driver).drag_and_drop(two_proess_loc,proess_box_loc).perform()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="dragTag_wrapper"]/section[2]/div/div[2]/a[1]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/section[2]/div[2]/div/div[2]/div/div/span[1]').click()
time.sleep(10)
