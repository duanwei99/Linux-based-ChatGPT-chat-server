from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction

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

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities=desired_caps)

time.sleep(1)

el1 = driver.find_element_by_xpath("//*[@text='通知']")
el2 = driver.find_element_by_xpath("//*[@text='WLAN']")

# 实例化TouchAction
action = TouchAction(driver )
# press 既可以使用 坐标 也可以使用元素

# 在移动的过程中 wait是必不可少
# action.press(el1).wait(500).move_to(el2)
action.press(x=270,y=640).wait(500).move_to(x=270,y=320)
action.release()

# 执行  模拟手势的使用  TouchAction 进行模拟手势的时候  一定要记得执行操作
action.perform()
time.sleep(3)

# 关闭app
driver.close_app()
# 释放资源
driver.quit()