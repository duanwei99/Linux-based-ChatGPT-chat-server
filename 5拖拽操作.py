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
desired_caps["appPackage"] = "com.vphone.launcher"
# 要启动的app的哪个界面
desired_caps["appActivity"] = ".launcher3.Launcher"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities=desired_caps)

time.sleep(1)
el1 = driver.find_element_by_xpath("//*[@text='酷安']")
el2 = driver.find_element_by_xpath("//*[@text='京东']")


driver.drag_and_drop(el1,el2)

time.sleep(2)

# 关闭app
driver.close_app()
# 释放资源
driver.quit()