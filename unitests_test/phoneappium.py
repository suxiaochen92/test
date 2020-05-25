from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

config={
    'deviceName':'PCT-AL10',
    'platformName':'Android',
    'platformVersion':'5.1.1',
    'appPackage':'io.appium.android.apis',
    'appActivity':'.ApiDemos',
    'unicodeKeyboard':True,
    'resetKeyboard':True
}
driver=webdriver.Remote('http://localhost:4723/wd/hub',config)
driver.find_element_by_accessibility_id('App').click()
driver.implicitly_wait(100)
e=driver.find_element_by_android_uiautomator('new UiSelector().text("Alarm")').text

time.sleep(3)
assert e=='Alarm'
print('测试通过')
time.sleep(3)
driver.back()
time.sleep(3)
driver.press_keycode(3)
time.sleep(3)
driver.swipe(143,810,766,810)
time.sleep(3)
driver.quit()