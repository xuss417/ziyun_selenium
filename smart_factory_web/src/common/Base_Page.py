#coding:utf-8

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.select import Select
from config.globalparameter import img_path
from src.common.log import Log
from selenium.common.exceptions import *
from src.common import log
from selenium.webdriver.common.action_chains import ActionChains

'''封装页面共用方法'''
class BasePage(object):
    #初始化浏览器
    def __init__(self,selenium_driver,base_url,page_title):
        self.driver = selenium_driver
        self.url = base_url
        self.title = page_title
        self.mylog = log.Log()
    #打开页面，验证链接打开页面是否正确
    def _open(self,url,page_title):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
            #断言输入的title是否在当前title中
            #assert page_title in self.driver.title, u'打开页面失败：%s' % url
        #这部分等加入日志后再来弄
        except:
            self.mylog.error(u'未能正确打开页面：'+url)

    #重写find_element方法

    def find_element(self,*loc):
        try:
            #WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc).is_displayed())

            return self.driver.find_element(*loc)
        except:
            self.mylog.error(u'找不到元素'+str(*loc))
    #重写send_key方法
    def send_keys(self,value,clear=True,*loc):
        try:
            if clear:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            self.mylog.error(u"输入失败,loc="+str(loc)+u'value='+value)

    #截图
    def img_screenshot(self,img_name):
        try:
            now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
            self.driver.get_screenshot_as_file("E:\\ziyun\\error_img\\"+now+'.png')
        except:
            self.mylog.error(u'截图失败：'+img_name)
    #文字是否在元素中
    def is_text_in_element(self,locator,text,timeout=10):
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except TimeoutException:
            self.mylog.error(u'元素上无该文字：'+str(locator))
    #是否存在
    def is_text_in_value(self,locator,value,timeout=10):
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(EC.text_to_be_present_in_element(locator, value))
            return result
        except TimeoutException:
            self.mylog.error(u'元素上无该值：' + str(locator))

    #判断元素选中状态
    def is_selected(self,locator,timeout =10):
        result = WebDriverWait(self.driver,timeout,1).until(EC.element_located_to_be_selected(locator))
        return result
    #判断元素的状态，selected是期望参数
    def is_selected_be(self,locator,selected=True,timeout =10):
        result = WebDriverWait(self.driver,timeout,1).until(EC.element_located_selection_state_to_be(locator,selected))
        return result
    #判断页面是否有alert
    def is_alert_present(self,timtout=10):
        result = WebDriverWait(self.driver,timtout,1).until(EC.alert_is_present())
        return result
    #判断元素是否可点击
    def is_clickable(self,locator,timeout=10):
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_to_be_clickable(locator))
        return result
    #鼠标悬停操作
    def move_to_element(self,locator):
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    #鼠标拖拽元素
    def drag_and_drop(self,locator1,locator2):
        dragger1 =self.find_element(locator1)
        dragger2 = self.find_element(locator2)
        ActionChains(self.driver).drag_and_drop(dragger1, dragger2).perform()


    #执行js
    def js_execute(self,js):
        return self.driver.execute_script(js)
    #滚动到顶部
    def js_scroll_top(self):
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)
    #滚动到顶部
    def js_scroll_end(self):
        try:
            js = "window.scrollTo(0,document.body.scrollHeight)"
            self.driver.execute_script(js)
        except:
            self.mylog.error(u'滚动滑动条到顶部失败')
    #通过索引，选中下拉框元素值
    def select_by_index(self,locator,index):
        try:
            element =self.find_element(locator)
            Select(element).select_by_index(index)
        except:
            self.mylog.error(u'下拉框index无此内容：' + str(index))
    #通过下拉框值选中元素
    def select_by_value(self,locator,value):
        element = self.find_element(locator)
        Select(element).select_by_value(value)
    #通过文本内容定位
    def select_by_text(self,locator,text):
        element = self.find_element(locator)
        Select(element).select_by_value(text)





