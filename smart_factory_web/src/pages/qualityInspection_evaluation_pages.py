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


class evaluation_Page(BasePage):
    # 定位器

    # 质检评估
    zhijianevalution_btn = (By.XPATH, '/html/body/div[1]/div[2]/ul/li[5]/a/span')
    scanCode_tuzhi = (By.XPATH, '/html/body/div[2]/div')
    reworkchoies =(By.XPATH,'//*[@id="exceptional_container"]/dl/dd/span[1]/i')
    scrapchoies = (By.XPATH,'//*[@id="exceptional_container"]/dl/dd/span[2]/i')
    evaluatisurebtn=(By.ID,'sumbmit_btn')
    # 质检评估返工
    def evaluation_rework(self, productionplannumber):
        # self._open(self.url, self.title)
        # self.find_element(*self.loginwords_loc).click()
        self.find_element(*self.zhijianevalution_btn).click()
        self.find_element(*self.scanCode_tuzhi).send_keys(productionplannumber)
        self.find_element(*self.reworkchoies).click()
        self.find_element(*self.evaluatisurebtn).click()

    # 质检评估报废
    def evaluation_scrap(self, productionplannumber):
        # self._open(self.url, self.title)
        # self.find_element(*self.loginwords_loc).click()
        self.find_element(*self.zhijianevalution_btn).click()
        self.find_element(*self.scanCode_tuzhi).send_keys(productionplannumber)
        self.find_element(*self.scrapchoies).click()
        self.find_element(*self.evaluatisurebtn).click()

