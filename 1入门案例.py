from appium import webdriver
import time
# 连接移动设备所必须的参数
desired_caps = {}

# 当前要测试的设备的名称
desired_caps["deviceName"] = "127.0.0.1:62001"
# 系统
desired_caps["platformName"] = "Android"
# 系统的版本
desired_caps["platformVersion"] = "7.1"
# 要启动app的名称(包名)
desired_caps["appPackage"] = "com.android.settings"
# 要启动的app的哪个界面
desired_caps["appActivity"] = ".Settings"

desired_caps["automationName"] = "UiAutomator2"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_caps)

time.sleep(5)
# print(driver.page_source)

# 关闭app
driver.terminate_app("com.android.settings")
# 释放资源
driver.quit()