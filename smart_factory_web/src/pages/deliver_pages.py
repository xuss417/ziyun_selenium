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

class deliver_Page(BasePage):
    #定位
    #交付
    deliver_btn = (By.XPATH, '/html/body/div[1]/div[2]/ul/li[2]/a/span')
    deliver_tuzhi = (By.XPATH, '//*[@id="scan_div"]/div')
    deliver_scroll = (By.XPATH,'html/body/div[4]')
    deliver_surebtn = (By.ID, 'submit_btn')
    #异常交付
    deliver_exceptionalchoise = (By.XPATH, 'html/body/div[4]/div[3]/div[1]/ul/li[2]/a/i')
    deliver_exceptionaladd = (By.ID, 'exceptional_add_btn')
    deliver_exceptionalinput = (By.XPATH, '//*[@id="exceptional_container"]/span/input')


    # 工人正常生产
    def Ndeliver(self,productionplannumber):
        self.find_element(*self.deliver_btn).click()
        self.find_element(*self.deliver_tuzhi).send_keys(productionplannumber)
        self.find_element(*self.deliver_surebtn).click()

    def Edeliver(self,productionplannumber,exceptionalname):
        self.find_element(*self.deliver_btn).click()
        self.find_element(*self.deliver_tuzhi).send_keys(productionplannumber)
        self.find_element(*self.deliver_exceptionalchoise).click()
        self.find_element(*self.deliver_exceptionaladd).click()
        self.find_element(*self.deliver_exceptionalinput).send_keys(exceptionalname)
        self.find_element(*self.deliver_surebtn).click()