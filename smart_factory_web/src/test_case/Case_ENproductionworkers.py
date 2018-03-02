# coding:utf-8
import sys,time
import unittest
from selenium import webdriver
from src.pages.wokerlogin import loginPage
from src.pages.receive_pages import receive_Page
from src.pages.scanCod_pages import scancode_Page
from src.pages.deliver_pages import deliver_Page
from src.pages.quality_pages import quality_Page
from src.pages.qualityInspection_evaluation_pages import evaluation_Page
from time import sleep
#页面测试用例
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.loginurl = 'https://iot.qa.ziyun-cloud.net/manufacture/login.html'
        self.url = 'https://iot.qa.ziyun-cloud.net/manufacture/index.html'
        #self.url ='http://www.ziyun-cloud.com/service/smf-prod/login.html'
        self.driver.maximize_window()
        #声明NPWpage类对象
        self.workerloginpages = loginPage(self.driver,self.loginurl,'u')
        self.receive_pages = receive_Page(self.driver,self.url,'u')
        self.scancode_pages = scancode_Page(self.driver,self.url,'u')
        self.deliver_pages = deliver_Page(self.driver,self.url,'u')
        self.quality_pages = quality_Page(self.driver,self.url,'u')
        self.evalution_pages = evaluation_Page(self.driver,self.url,'u')
    #测试用例
    def test_ENPRODUCTION(self):
        #工人

        self.workerloginpages.login('ZY000232815196','123456')

        #self.receive_pages.Nreceive('1794')

        #self.scancode_pages.Nscancodeprodction('232','1794')

        #self.deliver_pages.Edeliver('1794','0001')

        #self.deliver_pages.Ndeliver('1794')
        #质检人员普通质检
        self.workerloginpages.login('ZY000231815196','123456')
        #self.receive_pages.Nreceive('1794')

        #self.quality_pages.Ezhijian_workers('1794','z002')
        #self.deliver_pages.Ndeliver('1794')
        #质检评估
        #self.receive_pages.Ereceive('1794')

        #self.evalution_pages.evaluation_rework('1794')

        #特殊质检
        self.quality_pages.Eexzhijian_workers('1794')
        time.sleep(5)

    def tearDown(self):
        self.driver.close()