from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver=webdriver.Chrome(executable_path='chromedriver.exe')
# driver.maximize_window()
driver.get('http://www.baidu.com')

# driver.find_element_by_name('wd').send_keys('七龙珠')
# driver.implicitly_wait(100)
# driver.find_element_by_id('id').click()

name=('name','wd')
id=('id','su')
WebDriverWait(driver,100).until(lambda s:s.find_element(*name)).send_keys('七龙珠')
WebDriverWait(driver,100).until(lambda s:s.find_element(*id)).click()

time.sleep(3)
assert driver.title=='七龙珠_百度搜索'
print(driver.current_url)
time.sleep(3)
driver.quit()

driver.swtch_to_alert().accept()
driver.swtch_to_alert().dismiss()
driver.switch_to_frame('idzhi')
driver.switch_to_window(driver.window_handles[-1])