# coding:utf-8

import unittest
from selenium import webdriver
from src.pages.LogininPage import LoginPage
from time import sleep
from src.common.log import Log
log = Log()
#页面测试用例

class TestLogin(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome()
        self.url = 'https://iot.qa.ziyun-cloud.net/new_factory/login.html'
        #声明loginpage类对象
        self.login_page = LoginPage(self.driver,self.url,u'无tile')

    #测试用例
    def test_login1(self):
        log.info("测试用例开始")
        self.login_page.open()
        self.login_page.logingM()

    def tearDown(self):
        log.info("测试用例结束")
        self.driver.close()
