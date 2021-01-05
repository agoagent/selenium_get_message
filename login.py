#coding:utf-8
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
import sys,os

# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# driver = webdriver.PhantomJS(executable_path=r'D:\work_station\phantomjs-2.1.1-windows\bin\phantomjs.exe') # 此浏览器已停用，使用浏览器,已配置了环境变量可以直接使用

# -*- coding: utf-8 -*-
#用于实现将数据设置到剪贴板中

import win32clipboard as w
import win32con

class Clipboard():
    """
    模拟Windows设置剪贴板
    """
    # 读取剪贴板
    @staticmethod
    def getText():
        # 打开剪贴板
        w.OpenClipboard()
        # 读取剪贴板中的数据
        d = w.GetClipboardData(win32con.CF_UNICODETEXT)
        # 关闭剪贴板
        w.CloseClipboard()
        # 将读取的数据返回，提供给调用者
        return d

    # 设置剪贴板内容
    @staticmethod
    def setText(aString):
        # 打开剪贴板
        w.OpenClipboard()
        # 清空剪贴板
        w.EmptyClipboard()
        # 将数据astring写入剪贴板中
        w.SetClipboardData(win32con.CF_UNICODETEXT,aString)
        # 关闭剪贴板
        w.CloseClipboard()

#整合
def ChromeDriverBrowser(display):
    # path = 'D:/free_sofe_ware/MyChrome_v3.8.1_x64/MyChrome.exe' //正式使用版本
    # path = "D:/free_sofe_ware/MyChrome_v3.8.1_x64/Chrome/chrome.exe"
    if(display == 0):
        # 无界面模式 #有bug，无法进行第四步
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        # driver = webdriver.Chrome(executable_path=path,chrome_options=chrome_options)
        driver = webdriver.Chrome(chrome_options=chrome_options)
    else:
        # 有界面的
        # driver = webdriver.Chrome(executable_path=path)
        driver = webdriver.Chrome()
    return driver

def check_downloads_done():
    for i in os.listdir(r"D:\MyData\pengjw3\Downloads"):
        if ".crdownload" in i:
            time.sleep(0.5)

def find_folder(file_path, target_folder_name):
    father_folder_list = os.listdir(file_path)
    for folder in father_folder_list:
        if target_folder_name in folder:
            return file_path+'/'+folder

#选择界面 0无 1有
display = 1
save_pic_path = "./pics/"
driver = ChromeDriverBrowser(display)
driver.set_window_size(1680,1050)
driver.maximize_window()

driver.get("********") # 打开目标网站
driver.save_screenshot(save_pic_path+"login.png") # 获取截图,保存为__自定义__.png
True                               # true表示截图获取成功

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_load(input_type,target,time = 10): 
    # input_type ： By.XPATH
    type_dic = {'ID':By.ID, 'XPATH':By.XPATH, 'CSS_SELECTOR':By.CSS_SELECTOR}
    for key,value in type_dic.items():
        if(key == input_type):
            input_type = value
    try:
        WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((input_type,target)))        
        # text = driver.page_source
        # print("text", text)
    except:
        print('no infmation:'+input_type+','+target)
        driver.quit()
 
# 注意:windows下  截图默认保存在 C:\user\user_name  你的用户目录下
from selenium.webdriver.common.keys import Keys     # 导入common包可以操作html标签
from selenium.webdriver.common.action_chains import ActionChains #鼠标悬停


if display == 0: 
    #未完成
    print("nodisplay")
    check_load('XPATH', '/html/body/div[1]/div/div/a')
    #鼠标悬浮并选择简中
    ele = driver.find_element_by_xpath('/html/body/div[1]/div/div/a')
    ActionChains(driver).move_to_element(ele).perform()
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/ul/li[1]/a").click()
else:
    print("display")

#登录页
check_load('ID', 'username')
driver.find_element_by_id("username").send_keys(u"pengjw3")   # 通过审查元素发现input标签id为__查询网站__，输入账号
driver.find_element_by_id("password").send_keys(u"pengjiaweijw3.2")   # 通过审查元素发现input标签id为__查询网站__，输入密码 
driver.save_screenshot(save_pic_path+"list.png")  # 保存截图
True
driver.find_element_by_id("password").send_keys(Keys.ENTER) # 模拟Enter回车键

#信息主页
check_load('CSS_SELECTOR','div.el-table__body-wrapper.is-scrolling-none')

link_lists = driver.find_elements_by_css_selector('div.el-table__body-wrapper.is-scrolling-none>table>tbody>tr>td.el-table_1_column_1>div>a')
td_lists = driver.find_elements_by_css_selector('div.el-table__body-wrapper.is-scrolling-none>table>tbody>tr>td.el-table_1_column_3')
test_count = 0

for link_key,link_list in enumerate(link_lists):
    for td_key,td_list in enumerate(td_lists):
        if(td_list.text == '计划员确认'):
            if(link_key == td_key):
                time.sleep(1)
                check_load('CSS_SELECTOR','div.el-table__body-wrapper.is-scrolling-none')
                target_pic_path = save_pic_path+"inf_link"+str(link_key)+".png"
                link_list.click()
                check_load('CSS_SELECTOR','div.el-table__body-wrapper.is-scrolling-none')
                driver.save_screenshot(target_pic_path)
                
                time.sleep(1)
                inf_link = driver.find_element_by_css_selector('div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr > td > div > a')
                inf_link_text = inf_link.text
                inf_link.click()
                check_load('CSS_SELECTOR','#pane-BASIC_ATTR')
                driver.save_screenshot(target_pic_path)

                # 核心部分_获取信息
                test_projects_value = '//*[text()="导出委托项"]/..'
                test_projects = driver.find_elements_by_xpath(test_projects_value)
                test_project = test_projects[-1]
                if(test_count != 0 ):
                    test_information = driver.find_element_by_xpath('//*[text()="批量下载"]')
                else:
                    test_informations = driver.find_elements_by_xpath('//*[text()="批量下载"]')
                    test_information = test_informations[-1]
                target_folder = find_folder(r'D:\work_station\doc_auto\Auto_Selenium\Report',inf_link_text)
                if(target_folder):
                    target_project_folder = find_folder(target_folder,'information')
                    if not(target_project_folder):
                        time.sleep(1)
                        test_project.click()
                    target_information_folder = find_folder(target_folder,'委托资料')
                    if not(target_information_folder):
                        time.sleep(1)
                        test_information.click()
                else:
                    time.sleep(1)
                    test_project.click()
                    time.sleep(1)
                    test_information.click()
                check_downloads_done()

                #选择数据复制到剪切板再获取并写入文件
                driver.find_element_by_css_selector('body').send_keys(Keys.CONTROL,'a')
                time.sleep(1)
                driver.find_element_by_css_selector('body').send_keys(Keys.CONTROL,'c')
                value = Clipboard.getText()
                time.sleep(1)

                with open(r"D:\work_station\doc_auto\Auto_Selenium\File_change\auto_file_in.txt",'w',encoding='utf-8') as get_value:
                    get_value.write(value)

                #执行报告生成项目
                import os
                os.system("python D:/work_station/doc_auto/Auto_Selenium/main.py")
                #----

                check_load('CSS_SELECTOR','#app > div > div.main-container > div.sidebar-container > aside > div > ul > li')
                driver.find_element_by_css_selector('#app > div > div.main-container > div.sidebar-container > aside > div > ul > li').click()
                check_load('CSS_SELECTOR','div.el-table__body-wrapper.is-scrolling-none')

driver.quit()     # 关闭浏览器