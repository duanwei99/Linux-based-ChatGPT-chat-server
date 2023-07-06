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

# 获取当前屏幕的分辨率
size = driver.get_window_size()
print(size)
width = size["width"]
height = size["height"]

driver.swipe(start_x=width/2,start_y=height/3*2,end_x=width/2,end_y=height/3)

# el1 = driver.find_element_by_xpath("//*[@text='通知']")
# el2 = driver.find_element_by_xpath("//*[@text='WLAN']")
#
#使用driver的方法在不同手机分辨率的手机上有更强的适应性
# driver.scroll(el1,el2)
time.sleep(2)



# 关闭app
driver.close_app()

time.sleep(2)
# 释放资源
driver.quit()