'''
case:templemanagement practice in ecshop back page(backpage management)
'''

#import webdriver
from  selenium import  webdriver
from selenium.webdriver.common.by import By
import time

#open chrome
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)

#open ecshop front page
driver.get("http://localhost/upload/admin/privilege.php?act=login")
time.sleep(2)

#login
driver.find_element_by_name('username').send_keys("admin")
driver.find_element_by_name('password').send_keys("wd19960315")
driver.find_element_by_class_name('button').click()
time.sleep(3)

#get in temple select
#//*[@id="menu-ul"]/li[10]
driver.switch_to.frame('menu-frame')
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[10]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[10]/ul/li[1]/a').click()
time.sleep(1)
driver.switch_to.default_content()

#select temple
driver.switch_to.frame('main-frame')
driver.find_element(By.XPATH,'//img[@id="ecmoban_meilishuo"]').click()
time.sleep(2)
driver.switch_to.alert.dismiss()
time.sleep(2)
driver.find_element(By.XPATH,'//img[@id="ecmoban_meilishuo"]').click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)
driver.switch_to.default_content()

#close and quit
time.sleep(2)
driver.quit()