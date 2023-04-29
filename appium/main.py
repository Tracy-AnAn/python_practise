# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from appium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy as By
import datetime

desired_caps = {
    "platformName": "Android",
    "appium:platformVersion": "7.1.2",
    "appium:deviceName": "SM_G9810",
    # "appium:appPackage": "com.jingdong.app.mall",
    # "appium:appActivity": ".MainFrameActivity",
    "unicodeKeyboard": True,
    "resetKeyboard": True,
}

# 连上模拟器
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 点击京东
xpath = r'//android.widget.TextView[@content-desc="京东"]'
WebDriverWait(driver, 2, 0.5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
driver.find_element_by_xpath(xpath).click()

# 点击搜索框进入搜索界面
xpath = r'//android.widget.TextView[contains(@content-desc, "搜索框")]'
WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
driver.find_element_by_xpath(xpath).click()

# 搜索框输入“茅台飞天53度”
xpath = r'//android.widget.EditText[contains(@content-desc, "搜索框")]'
WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
driver.find_element_by_xpath(xpath).send_keys("茅台飞天53度")

# 点击搜索按钮
xpath = r'//android.widget.TextView[@content-desc="搜索，按钮"]'
WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
driver.find_element_by_xpath(xpath).click()

# 点击商品
xpath = r'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.' \
        r'FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView' \
        r'/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout'

# 随便找一个抢下试试
# xpath = r'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.' \
#         r'DrawerLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.' \
#         r'RelativeLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout'
WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
driver.find_element_by_xpath(xpath).click()

# 点击立刻抢购
startTime = datetime.datetime(2023, 4, 16, 11, 59, 50)
print(startTime)
id = 'com.jd.lib.productdetail.feature:id/add_2_car'
while datetime.datetime.now() < startTime:
    sleep(0.5)
    print(datetime.datetime.now())
WebDriverWait(driver, 300, 0.1).until(EC.visibility_of_element_located((By.ID, id)))
driver.find_element_by_id(id).click()

# 点击确定
id = 'com.jd.lib.productdetail.feature:id/detail_style_left_btn'
WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.ID, id)))
driver.find_element_by_id(id).click()

# 点击提交订单
id = 'com.jd.lib.settlement.feature:id/a38'
WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.ID, id)))
driver.find_element_by_id(id).click()

# 点击返回
id = 'com.jingdong.app.mall:id/a93'
WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.ID, id)))
driver.find_element_by_id(id).click()

# 点击稍后再支付
xpath = r'//*[@text="稍后再支付"]'
WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
driver.find_element_by_xpath(xpath).click()

# 点击确认离开
id = 'com.jingdong.app.mall:id/bq'
WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.ID, id)))
driver.find_element_by_id(id).click()
