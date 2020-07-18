'''
case:templemanagement practice in ecshop back page(backpage management)
'''

#import webdriver
from  selenium import  webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#set var
username = "manager1"
email = "555@qq.com"
pwd = "ma123456"
pwd_confirm = "ma123456"
nemail = "888@qq.com"

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

#get in manager list
#//*[@id="menu-ul"]/li[8]
driver.switch_to.frame('menu-frame')
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[8]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[8]/ul/li[1]/a').click()
time.sleep(1)
driver.switch_to.default_content()

#add manager
driver.switch_to.frame('main-frame')
WebDriverWait(driver,5,1).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,'添加管理员')))
driver.find_element(By.XPATH,'//span[@class="action-span"]/a').click()
time.sleep(1)
driver.find_element(By.NAME,'user_name').send_keys(username)
time.sleep(1)
driver.find_element(By.NAME,'email').send_keys(email)
time.sleep(1)
driver.find_element(By.NAME,'password').send_keys(pwd)
time.sleep(1)
driver.find_element(By.NAME,'pwd_confirm').send_keys(pwd_confirm)
time.sleep(1)

# #reset
# driver.find_element(By.XPATH,'//form[@name="theForm"]/table/tbody/tr[5]/td/input[2]').click()

#confirm
driver.find_element(By.XPATH,'//form[@name="theForm"]/table/tbody/tr[5]/td/input[1]').click()
time.sleep(5)
# #back to managerlist
# #/html/body/h1/span[1]/a
# driver.find_element(By.XPATH,'/html/body/h1/span[1]/a').click()

#select power

#submit power
driver.find_element(By.XPATH,'//table[@id="list-table"]/tbody/tr[12]/td/input[2]').click()
time.sleep(5)

#get in edit
driver.find_element(By.XPATH,'//table[@id="list-table"]/tbody/tr[2]/td[5]/a[3]/img').click()
time.sleep(2)

#edit
driver.find_element(By.NAME,'user_name').send_keys('ad')
time.sleep(1)
driver.find_element(By.NAME,'email').clear()
driver.find_element(By.NAME,'email').send_keys(nemail)
time.sleep(1)
driver.find_element(By.NAME,'old_password').send_keys(pwd)
time.sleep(1)
driver.find_element(By.NAME,'new_password').send_keys('ad123456')
time.sleep(1)
driver.find_element(By.NAME,'pwd_confirm').send_keys('ad123456')
time.sleep(1)
driver.find_element(By.XPATH,'//form[@name="theForm"]/table/tbody/tr[6]/td/input[1]').click()
time.sleep(5)

#delete
driver.find_element(By.XPATH,'//table[@id="list-table"]/tbody/tr[2]/td[5]/a[4]/img').click()
time.sleep(2)
#cancel delete
driver.switch_to.alert.dismiss()
time.sleep(1)
#confirm delete
driver.find_element(By.XPATH,'//table[@id="list-table"]/tbody/tr[2]/td[5]/a[4]/img').click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(1)

driver.switch_to.default_content()

#close and quit
time.sleep(2)
driver.quit()