#!/usr/bin/env python

import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
cap = {
  "platformName": "Android",
  "platformVersion": "4.4.2",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "com.ss.android.ugc.aweme",
  "appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
  "noReset": True,
  "unicodeKeyboard":True,
  "resetkeyboard":True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",cap)

def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return(x,y)


try:
    #点击搜索
    print('点击搜索')
    if WebDriverWait(driver,60).until(lambda x:x.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.widget.ImageView[1]")):
        driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()
except:
    #[26,76][115,165]
    driver.tap([(26,76),(115,165)],500)
#定位搜索框
if WebDriverWait(driver,60).until(lambda x:x.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.EditText[1]")):
    #获取douyin_id进行搜索
    driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.EditText[1]").send_keys('191433445')
    while driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.EditText[1]").text != '191433445':
        driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.EditText[1]").send_keys('191433445')
        time.sleep(0.1)
#点击搜索
driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()


#点击用户标签
if WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath("//android.widget.TextView[@text='用户']")):
    driver.find_element_by_xpath("//android.widget.TextView[@text='用户']").click()
#点击头像
if WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.view.View[1]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]")):
    driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.view.View[1]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
#点击粉丝按钮
if WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[5]/android.widget.LinearLayout[3]/android.widget.TextView[2]")):
    driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[5]/android.widget.LinearLayout[3]/android.widget.TextView[2]").click()


    x1 = int(driver.get_window_size()['width']*0.5)
    y1 = int(driver.get_window_size()['height']*0.75)
    y2 = int(driver.get_window_size()['height']*0.25)
    while True:
        if '没有更多了' in driver.page_source:
            break
        driver.swipe(x1,y1,x1,y2)
        time.sleep(0.5)