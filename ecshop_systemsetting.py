'''
case:systemsetting practice in ecshop back page(backpage management)
'''

#import webdriver
from  selenium import  webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

#open chrome
driver = webdriver.Chrome()
driver.implicitly_wait(6)
driver.maximize_window()

#open ecshop front page
driver.get("http://localhost/upload/admin/privilege.php?act=login")

#login
driver.find_element_by_name('username').send_keys("admin")
driver.find_element_by_name('password').send_keys("wd19960315")
driver.find_element_by_class_name('button').click()

#get in system setting
WebDriverWait(driver,5,1).until(expected_conditions.presence_of_element_located((By.TAG_NAME,'frame')))
driver.switch_to.frame('menu-frame')
WebDriverWait(driver,5,1).until(expected_conditions.presence_of_element_located((By.XPATH,'//ul[@id="menu-ul"]/li[9]')))
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[9]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[9]/ul/li[1]/a').click()
time.sleep(1)
driver.switch_to.default_content()
#setting system
driver.switch_to.frame('main-frame')
driver.find_element(By.XPATH,'//table[@id="shop_info-table"]/tbody/tr[1]/td[2]/input').clear()
time.sleep(1)
driver.find_element(By.XPATH,'//table[@id="shop_info-table"]/tbody/tr[1]/td[2]/input').send_keys('young')
time.sleep(1)
ele = driver.find_element(By.ID,'selCountries')
select = Select(ele)
select.select_by_value('1')
time.sleep(1)
ele1 = driver.find_element(By.ID,'selProvinces')
select1 = Select(ele1)
select1.select_by_visible_text('四川')
time.sleep(1)
ele2 = driver.find_element(By.ID,'selCities')
select2 = Select(ele2)
select2.select_by_visible_text('成都')
time.sleep(1)
#C:\Users\Administrator\Desktop
driver.find_element(By.NAME,'shop_logo').send_keys('C:\\Users\Administrator\Desktop\logo.gif')
time.sleep(1)
driver.find_element(By.ID,'value_119_0').click()
time.sleep(1)
driver.execute_script('window.scrollTo(100,300)')
time.sleep(1)
driver.find_element(By.XPATH,'//div[@id="tabbody-div"]/form/div/input[1]').click()
time.sleep(1)
driver.switch_to.default_content()

#adduser setting
#get in
driver.switch_to.frame('menu-frame')
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[9]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[9]/ul/li[2]/a').click()
time.sleep(1)
driver.switch_to.default_content()
#setting
driver.switch_to.frame('main-frame')
driver.find_element(By.XPATH,'/html/body/h1/span[1]/a').click()
time.sleep(1)
driver.find_element(By.NAME,'reg_field_name').send_keys('hobby')
time.sleep(1)
driver.find_element(By.NAME,'reg_field_order').clear()
driver.find_element(By.NAME,'reg_field_order').send_keys('80')
time.sleep(1)
driver.find_elements(By.NAME,'reg_field_display')[0].click()
time.sleep(1)
driver.find_elements(By.NAME,'reg_field_need')[1].click()
time.sleep(1)
driver.find_element(By.XPATH,'//form[@name="theForm"]/table/tbody/tr[5]/td[2]/input[4]').click()
time.sleep(5)
#edit
driver.find_element(By.XPATH,'//table[@id="list-table"]/tbody/tr[8]/td[5]/a[1]').click()
time.sleep(3)
driver.find_element(By.NAME,'reg_field_name').clear()
driver.find_element(By.NAME,'reg_field_name').send_keys('dislike')
time.sleep(1)
driver.find_element(By.NAME,'reg_field_order').clear()
driver.find_element(By.NAME,'reg_field_order').send_keys('90')
time.sleep(1)
driver.find_elements(By.NAME,'reg_field_display')[0].click()
time.sleep(1)
driver.find_elements(By.NAME,'reg_field_need')[0].click()
time.sleep(1)
driver.find_element(By.XPATH,'//form[@name="theForm"]/table/tbody/tr[5]/td[2]/input[4]').click()
time.sleep(5)
#delete
driver.find_element(By.XPATH,'//table[@id="list-table"]/tbody/tr[8]/td[5]/a[2]').click()
time.sleep(1)
driver.switch_to.alert.dismiss()
time.sleep(1)
driver.find_element(By.XPATH,'//table[@id="list-table"]/tbody/tr[8]/td[5]/a[2]').click()
time.sleep(1)
driver.switch_to.alert.accept()
time.sleep(1)
driver.switch_to.default_content()

#add payways
#get in
driver.switch_to.frame('menu-frame')
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[9]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[9]/ul/li[3]/a').click()
time.sleep(1)
driver.switch_to.default_content()
#add
driver.switch_to.frame('main-frame')
#//*[@id="listDiv"]/table/tbody/tr[2]/td[7]/a alipay
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[2]/td[7]/a').click()
time.sleep(3)
#/html/body/form/div/table/tbody/tr[10]/td/input[5] confirm alipay
driver.find_element(By.XPATH,'//div[@class="main-div"]/table/tbody/tr[10]/td/input[5]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[2]/td[7]/a[1]').click()
time.sleep(1)
driver.switch_to.alert.dismiss()
time.sleep(1)
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[2]/td[7]/a[1]').click()
time.sleep(1)
driver.switch_to.alert.accept()
time.sleep(1)
driver.switch_to.default_content()

#add sendways
#get in
driver.switch_to.frame('menu-frame')
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[9]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[9]/ul/li[4]/a').click()
time.sleep(1)
driver.switch_to.default_content()
#add
driver.switch_to.frame('main-frame')
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[6]/td[8]/a').click()
time.sleep(5)
driver.find_element(By.NAME,'shipping_area_name').send_keys('国内')
time.sleep(1)
driver.find_element(By.NAME,'free_money').clear()
driver.find_element(By.NAME,'free_money').send_keys('9')
time.sleep(1)
ele3 = driver.find_element(By.ID,'selCountries')
select3 = Select(ele3)
select3.select_by_visible_text('中国')
time.sleep(1)
driver.find_element(By.XPATH,'//form[@name="theForm"]/fieldset[2]/table/tbody/tr[2]/td/span[5]/input').click()
time.sleep(1)
driver.find_element(By.XPATH,'//form[@name="theForm"]/table/tbody/tr/td/input[1]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//span[@id="search_id"]/a').click()
time.sleep(3)
#edit
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[6]/td[8]/a[2]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//span[@id="search_id"]/a').click()
time.sleep(3)
#delete
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[6]/td[8]/a[1]').click()
time.sleep(1)
driver.switch_to.alert.dismiss()
time.sleep(1)
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[6]/td[8]/a[1]').click()
time.sleep(1)
driver.switch_to.alert.accept()
time.sleep(1)
driver.switch_to.default_content()

#close and quit
time.sleep(2)
driver.quit()