'''
case:login practice in ecshop front page
'''

#import webdriver
from  selenium import  webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


#open chrome
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)

#open ecshop front page
driver.get("http://localhost/upload/index.php")
time.sleep(2)

#login
#//*[@id="ECS_MEMBERZONE"]/a[1]
WebDriverWait(driver,5,1).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,'登录')))
driver.find_element(By.XPATH,'//font[@id="ECS_MEMBERZONE"]/a[1]').click()
time.sleep(2)
driver.find_element_by_name('username').send_keys("bu知道11")
driver.find_element_by_name('password').send_keys("123456")
driver.find_element_by_name('submit').click()
time.sleep(3)

#close and quit
time.sleep(2)
driver.quit()