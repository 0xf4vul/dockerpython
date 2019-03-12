#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 15:11
# @Author  : Aries
# @Site    : 
# @File    : aaa.py
# @Software: PyCharm

from appium import webdriver

cap = {
        "platformName": "Android",
        "platformVersion": "4.4.2",
        "deviceName": "192.168.1.120:55555",
        "udid":"192.168.1.120:55555",
        # 真机的
        # "platformName": "Android",
        # "platformVersion": "7.1.2",
        # "deviceName": "10d4e4387d74",
        "appPackage": "com.ss.android.ugc.aweme",
        "appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
        "noReset": True,
        "unicodeKeyboard": True,
        "resetkeyboard": True
    }

driver = webdriver.Remote("http://192.168.70.100:4723/wd/hub", cap)