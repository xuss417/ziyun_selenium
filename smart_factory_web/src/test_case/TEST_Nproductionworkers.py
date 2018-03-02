# coding:utf-8
import sys,time
import unittest
from selenium import webdriver
from src.pages.Normal_productionworkersPage import Normal_productionworkersPage

from time import sleep
#页面测试用例
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = 'https://iot.qa.ziyun-cloud.net/manufacture/login.html'
        #声明NPWpage类对象
        self.Normal_productionworkers_page = Normal_productionworkersPage(self.driver,self.url,u' ')

    #测试用例
    def test_login1(self):
        try:
            self.Normal_productionworkers_page.production_workers('ZY000218215161','P1234','201','1527')

        except:
            self.Normal_productionworkers_page.img_screenshot(u'失败截图')
    def tearDown(self):
        self.driver.close()