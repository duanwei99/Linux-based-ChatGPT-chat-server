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

# driver.install_app(r"C:\Users\bcc\Desktop\pycode\appcode\iBiliPlayer-bili.apk")

if driver.is_app_installed("tv.danmaku.bili"):
    driver.remove_app("tv.danmaku.bili")

driver.find_element_by_xpath("//*[@resource-id='com.android.settings:id/search']").click()

time.sleep(1)
driver.find_element_by_xpath("//*[@resource-id='android:id/search_src_text']").send_keys("abc")
driver.find_element_by_xpath("//*[@resource-id='android:id/search_src_text']").send_keys("123")
driver.find_element_by_xpath("//*[@resource-id='android:id/search_src_text']").send_keys("张三")

time.sleep(2)
driver.find_element_by_xpath("//*[@resource-id='android:id/search_src_text']").clear()


# 关闭app
driver.close_app()

time.sleep(2)
# 释放资源
driver.quit()