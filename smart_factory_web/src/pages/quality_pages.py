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

class quality_Page(BasePage):
    #定位器

    #普通质检扫码作业
    scanCod_btn = (By.XPATH, '/html/body/div[1]/div[2]/ul/li[4]/a/i')
    scanCode_tuzhi = (By.XPATH, '/html/body/div[2]/div[2]')
    gzhijian =(By.XPATH,'//*[@id="skip_tip"]/div/div[2]/a[1]')
    excellent_input = (By.ID,'excellent_input')
    exceptional_add_btn =(By.ID,'exceptional_add_btn')
    exceptional_add_input =(By.XPATH,'//*[@id="exceptional_container"]/span/input')
    zhijiansub = (By.ID,'submit_btn')
    deliver_num = (By.ID, 'deliver_num')
   #特殊质检扫码作业
    exzhijian = (By.XPATH, '//*[@id="skip_tip"]/div/div[2]/a[2]')
    exzhijianexcellent=(By.XPATH,'//*[@id="exception_containal"]/dl/dd/span[1]/i')
    exzhijianbad =(By.XPATH,'//*[@id="exception_containal"]/dl/dd/span[3]/i')
    exzhijiansurebtn =(By.XPATH,'/html/body/div[2]/div[3]/div[4]/a')


    # 质检全正常
    def Nzhijian_workers(self,productionplannumber):
        #self._open(self.url, self.title)
        # self.find_element(*self.loginwords_loc).click()
        self.find_element(*self.scanCod_btn).click()
        self.find_element(*self.scanCode_tuzhi).send_keys(productionplannumber)
        self.find_element(*self.gzhijian).click()
        devicenum = self.find_element(*self.deliver_num).text
        self.find_element(*self.excellent_input).send_keys(devicenum)
        self.find_element(*self.zhijiansub).click()
    #普通质检含有差
    def Ezhijian_workers(self,productionplannumber,expname):
        self.find_element(*self.scanCod_btn).click()
        self.find_element(*self.scanCode_tuzhi).send_keys(productionplannumber)
        self.find_element(*self.gzhijian).click()
        devicenum = self.find_element(*self.deliver_num).text
        excellentunmber = int(devicenum) - 1
        self.find_element(*self.excellent_input).send_keys(excellentunmber)
        self.find_element(*self.exceptional_add_btn).click()
        self.find_element(*self.exceptional_add_input).send_keys(expname)
        self.find_element(*self.zhijiansub).click()
    #特殊质检无差
    def Nexzhijian_workers(self,productionplannumber):
        # self._open(self.url, self.title)
        # self.find_element(*self.loginwords_loc).click()
        self.find_element(*self.scanCod_btn).click()
        self.find_element(*self.scanCode_tuzhi).send_keys(productionplannumber)
        self.find_element(*self.exzhijian).click()
        self.find_element(*self.exzhijianexcellent).click()
        self.find_element(*self.exzhijiansurebtn).click()
    #特殊质检含有差
    def Eexzhijian_workers(self,productionplannumber):
        # self._open(self.url, self.title)
        # self.find_element(*self.loginwords_loc).click()
        self.find_element(*self.scanCod_btn).click()
        self.find_element(*self.scanCode_tuzhi).send_keys(productionplannumber)
        self.find_element(*self.exzhijian).click()
        self.find_element(*self.exzhijianbad).click()
        self.find_element(*self.exzhijiansurebtn).click()