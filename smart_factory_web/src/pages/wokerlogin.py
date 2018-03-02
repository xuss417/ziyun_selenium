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

class loginPage(BasePage):
    #定位器
    #登录
    username_loc = (By.ID, 'username')
    password_loc = (By.ID, 'pwd')
    loginsubmit_loc = (By.ID, 'sub_btn')

    # 工人正常生产
    def login(self,workerssoid,pwd):
        self._open(self.url, self.title)
        # self.find_element(*self.loginwords_loc).click()
        self.find_element(*self.username_loc).send_keys(workerssoid)
        self.find_element(*self.password_loc).send_keys(pwd)
        self.find_element(*self.loginsubmit_loc).click()
