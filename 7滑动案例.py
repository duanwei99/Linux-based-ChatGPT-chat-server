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

# el1 = driver.find_element_by_xpath("//*[@text='声音']")
# el2 = driver.find_element_by_xpath("//*[@text='蓝牙']")

action = TouchAction(driver)
# action.press(el1).wait(500).move_to(el2)
# action.release()
#
# # 需要执行上面的操作
# action.perform()
time.sleep(1)

# driver.find_element_by_xpath("//*[@text='安全']").click()
# time.sleep(1)
driver.find_element_by_xpath("//*[@text='设置屏幕锁定']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@text='图案']").click()
time.sleep(1)

# 按下的位置 105 450  x 165  y 165

action.press(x=105,y=450).wait(200).move_to(x=270,y=450).wait(200).move_to(x=435,y=450).wait(200).move_to(x=270,y=615)\
    .wait(200).move_to(x=105,y=780).wait(200).move_to(x=270,y=780).wait(200).move_to(x=435,y=780)
action.release()
action.perform()



time.sleep(2)
# 关闭app
driver.close_app()
# 释放资源
driver.quit()