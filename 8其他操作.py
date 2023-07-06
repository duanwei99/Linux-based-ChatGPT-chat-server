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

time.sleep(1)
# print(driver.page_source)
print(driver.device_time)

print(driver.network_connection)

driver.get_screenshot_as_file("jietu.png")

# driver.save_screenshot()
driver.open_notifications()

time.sleep(3)
# 关闭app
driver.close_app()
# 释放资源
driver.quit()