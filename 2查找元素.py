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

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities=desired_caps)

print(driver.current_package)
print(driver.current_activity)
time.sleep(1)
# print(driver.page_source)

# 在Android手机中 text并不是文本 而是属于标签的属性
# driver.find_element_by_xpath("//*[text()='显示']").click()

el= driver.find_element_by_xpath("//*[@text='显示']")

print(el.size)
print(el.text)
print(el.get_attribute("text"))
print(el.location)
time.sleep(1)
print(driver.current_package)
print(driver.current_activity)

time.sleep(3)
# 关闭app
driver.close_app()
# 释放资源
driver.quit()