import time
from selenium import webdriver
 
# path = "D:/free_sofe_ware/MyChromium/Chrome/chrome.exe"
# path = "D:/free_sofe_ware/MyChrome_v3.8.1_x64/Chrome/chrome.exe"
# path = "C:\Program Files (x86)\Microsoft\Edge Beta\Application\msedge.exe"
# driver = webdriver.PhantomJS(executable_path=r'D:\work_station\phantomjs-2.1.1-windows\bin\phantomjs.exe') # 使用浏览器,已配置了环境变量可以直接使用
# driver = webdriver.Chrome(executable_path=path)

driver = webdriver.Chrome()

driver.get("http://www.baidu.com/") # 打开百度

driver.save_screenshot("baidu.png") # 获取截图,保存为baidu.png
True                               # true表示截图获取成功
 
# 注意:windows下  截图默认保存在 C:\user\user_name  你的用户目录下
 
from selenium.webdriver.common.keys import Keys     # 导入common包可以操作html标签
 
driver.find_element_by_id("kw").send_keys(u"美女")   # 通过审查元素发现input标签中的输入搜索内容保存在"kw"中
 
driver.save_screenshot("./输出截图.png")  # 保存截图
True

# f = open('./data/'+localtime_file+' '+random_num+'.txt','w')
f = open("./输出结果.html",'w',encoding='utf-8')
f.write(driver.page_source)
f.close
print(driver.page_source) #获取源码
 
driver.get_cookies()  # 获取当前页面cookies
 
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a') # ctrl+a 全选输入框内容
 
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')   # ctrl+x 剪切输入框内容
 
driver.find_element_by_id("su").send_keys(Keys.RETURN)    # 模拟Enter回车键
 
driver.find_element_by_id("kw").clear()   # 清除输入框内容
 
driver.quit()     # 关闭浏览器