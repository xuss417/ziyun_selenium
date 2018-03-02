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

class scancode_Page(BasePage):
    #定位器
    #扫码作业
    scanCod_btn = (By.XPATH, '/html/body/div[1]/div[2]/ul/li[4]/a/i')
    scanCode_device = (By.XPATH,'/html/body/div[2]/div[1]')
    scanCode_tuzhi = (By.XPATH, '/html/body/div[2]/div[2]')
    scanCode_choiseE =(By.XPATH,'/html/body/div[2]/div[3]/div[1]/ul/li[2]/a/i')
    scanCode_surebtn = (By.XPATH, '/html/body/div[2]/div[5]/a')
    # 工人正常生产
    def Nscancodeprodction(self,devicename,productionplannumber):
        #self._open(self.url, self.title)
        # self.find_element(*self.loginwords_loc).click()
        self.find_element(*self.scanCod_btn).click()
        self.find_element(*self.scanCode_device).send_keys(devicename)
        self.find_element(*self.scanCode_tuzhi).send_keys(productionplannumber)
        self.find_element(*self.scanCode_surebtn).click()
    #异常加工
    def Escandeprodction(self,devicename,productionplannumber):
        # self._open(self.url, self.title)
        # self.find_element(*self.loginwords_loc).click()
        self.find_element(*self.scanCod_btn).click()
        self.find_element(*self.scanCode_device).send_keys(devicename)
        self.find_element(*self.scanCode_tuzhi).send_keys(productionplannumber)
        self.find_element(*self.scanCode_choiseE).click()
        self.find_element(*self.scanCode_surebtn).click()