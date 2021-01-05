from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #定义了变量EC表示expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element_by_css_selector('#kw').send_keys('python')
time.sleep(2)
try:
  WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,'su')))
  # WebDriverWait(driver,5,0.5) #5表示等待的最大时长秒单位，0.5位间隔秒
  # EC.presence_of_element_located((By.ID,'su')) #方法本身调用时有括号，所以调用时会有双括号填入参数
except:
  print('find not')
  driver.quit()
driver.find_element_by_id("su").send_keys(Keys.RETURN)
