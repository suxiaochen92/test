from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from config import *
import pymysql
import xlrd
import requests
import unittest
import selenium
from HTMLTestRunner import HTMLTestRunner
import traceback

a={
    'deviceName':'PCLM10',
    'platformName':'Android',
    'platformVersion':'5.1.1',
    'appPackage':'io.appium.android.apis',
    'appActivity':'.ApiDemos',
    'unicodeKeyboard':True,
    'resetKeyboard':True
}
driver=webdriver.Remote('http://localhost:4723/wd/hub',a)
a=('accessibility id','App')
b=('-android uiautomator','new UiSelector().text("Alarm")')
WebDriverWait(driver,100).until(lambda s:s.find_element(*a)).click()
e=WebDriverWait(driver,100).until(lambda s:s.find_element(*b)).text
time.sleep(3)
assert e=='Alarm'
print('True')
time.sleep(3)
driver.back()
time.sleep(3)
driver.press_keycode(3)
time.sleep(3)
driver.swipe(70,800,700,800)