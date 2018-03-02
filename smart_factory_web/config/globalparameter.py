# coding:utf-8
import time,os
'''globalparameter配置'''
#项目绝对路径
#project_path = "C:\\Users\\dell\Desktop\\ziyun\\"
#获取项目路径
project_path = "C:\\Users\\dell\Desktop\\git\\ziyunQA"

test_case_path = project_path + "\\src\\test_case"
test_data_path = project_path + "\\data"
log_path =  project_path + "\\log"
report_path =  project_path + "\\report\\"
report_name = report_path+time.strftime('%Y%m%d%H%S', time.localtime())
img_path = project_path+"\\error_img\\"+time.strftime('%Y%m%d%H%S', time.localtime())


# 设置发送测试报告的公共邮箱、用户名和密码
smtp_sever = 'smtp.ziyun-cloud.com'  # 邮箱SMTP服务，各大运营商的smtp服务可以在网上找，然后可以在foxmail这些工具中验正
email_name = "shasha.xu@ziyun-cloud.com"  # 发件人名称
email_password = "Xss123456"  # 发件人登录密码
email_To = 'weiwei.hao@ziyun-cloud.com'  # 收件人'''

