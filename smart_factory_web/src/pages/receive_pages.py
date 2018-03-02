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

class receive_Page(BasePage):
    #定位器
    #正常接收
    receive_btn = (By.XPATH,'/html/body/div[1]/div[2]/ul/li[3]/a/span')
    receive_tuzhi = (By.XPATH,'/html/body/div[2]/div')
    receive_surebtn=(By.ID,'submit_btn')
    #异常接收
    receive_choiseE=(By.XPATH,'/html/body/div[3]/div[3]/div[1]/ul/li[2]/a/i')
    transfer_btn = (By.XPATH, '/html/body/div[3]/div[2]/ul/li[9]/div/i[2]')
    receive_prosse = (By.XPATH,'/html/body/div[3]/div[2]/ul/li[3]/strong/div/div/div[1]')
    receive_prosse_choise =(By.XPATH,'/html/body/div[3]/div[2]/ul/li[3]/strong/div/div/div[2]/ul/li')
    # 工人正常接收
    def Nreceive(self,productionplannumber):
        #self._open(self.url, self.title)
        # self.find_element(*self.loginwords_loc).click()
        self.find_element(*self.receive_btn).click()
        self.find_element(*self.receive_tuzhi).send_keys(productionplannumber)
        self.find_element(*self.receive_surebtn).click()
        time.sleep(1)
    #异常接收
    def Ereceive(self,productionplannumber):
        self.find_element(*self.receive_btn).click()
        self.find_element(*self.receive_tuzhi).send_keys(productionplannumber)
        self.find_element(*self.receive_choiseE).click()
        self.find_element(*self.receive_prosse).click()
        self.find_element(*self.receive_prosse_choise).click()
        self.find_element(*self.receive_surebtn).click()
    def transfer_receive(self,productionplannumber):
        self.find_element(*self.receive_btn).click()
        self.find_element(*self.receive_tuzhi).send_keys(productionplannumber)
        self.find_element(*self.transfer_btn).click()
        self.find_element(*self.receive_surebtn).click()