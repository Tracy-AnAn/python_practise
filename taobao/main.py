from selenium import webdriver
import datetime
import time

# 启动谷歌浏览器的驱动器
driver = webdriver.Chrome()
# 最大化浏览器
driver.maximize_window()


# 传入用户名密码，登录淘宝
def login():
    # 打开淘宝
    driver.get("https://www.taobao.com")

    # 查找文本，登录
    if driver.find_element_by_link_text("亲，请登录"):
        driver.find_element_by_link_text("亲，请登录").click()

    print("请在30秒内完成扫码")
    time.sleep(30)

    driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)

    # 点击购物车里全选按钮
    if driver.find_element_by_id("J_SelectAll1"):
        driver.find_element_by_id("J_SelectAll1").click()
    time.sleep(3)
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(buytime):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if now == buytime:
            try:
                # 点击结算按钮
                if driver.find_element_by_id("J_Go"):
                    driver.find_element_by_id("J_Go").click()
                    print("结算成功")
                    submit()
            except:
                pass
        print(now)
        time.sleep(0.01)


def submit():
    while True:
        try:
            if driver.find_element_by_link_text('提交订单'):
                driver.find_element_by_link_text('提交订单').click()
                now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                print("抢购成功时间：%s" % now1)
                break
        except:
            print("再次尝试提交订单")
            time.sleep(0.01)


if __name__ == "__main__":
    # 登录
    login()
    # 设置抢购时间
    buy('2022-02-16 09:34:00')