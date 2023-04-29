from selenium import webdriver
import datetime
import time

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
from time import sleep

import os
import pickle

# 京东主页
jd_url = "https://www.jd.com/"
# 登录页
login_url = "https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F"
# 抢票目标页
target_url = 'https://detail.damai.cn/item.htm?spm=a2oeg.search_category.0.0.79864d152vgeML&id=709077524365&clicktitle=%E3%80%90%E5%A4%A7%E9%BA%A6%E3%80%91Tangoz%26%E7%AD%89%E4%B8%80%E4%B8%8B%E5%B0%B1%E5%9B%9E%E5%AE%B6%26JD%20%C2%B7%20%E7%8E%A9%E6%89%80%E6%9C%AA%E7%8E%A9'


class JD:
    def __init__(self):
        self.status = 0         # 状态,表示如今进行到何种程度
        self.login_method = 1   # {0:模拟登录,1:Cookie登录}自行选择登录方式
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')        # 默认Chrome浏览器


    def set_cookie(self):
        self.driver.get(jd_url)
        print("###请点击登录###")
        while self.driver.title.find('京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！') != -1:
            sleep(1)
        print('###请扫码登录###')

        while self.driver.title.find('京东-欢迎登录') != -1:
           sleep(1)
        print("###扫码成功###")
        pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))
        print("###Cookie保存成功###")
        self.driver.get(target_url)

    def get_cookie(self):
        try:
            cookies = pickle.load(open("cookies.pkl", "rb"))  # 载入cookie
            for cookie in cookies:
                cookie_dict = {
                    'domain':'.damai.cn',  # 必须有，不然就是假登录
                    'name': cookie.get('name'),
                    'value': cookie.get('value')
                }
                self.driver.add_cookie(cookie_dict)
            print('###载入Cookie###')
        except Exception as e:
            print(e)

    def login(self):
        if self.login_method==0:
            self.driver.get(login_url)
            # 载入登录界面
            print('###开始登录###')

        elif self.login_method==1:
            if not os.path.exists('cookies.pkl'):
                # 如果不存在cookie.pkl,就获取一下
                self.set_cookie()
            else:
                self.driver.get(target_url)
                self.get_cookie()

    def enter_jd(self):
        """打开浏览器"""
        print('###打开浏览器，进入京东网###')
        # self.driver.maximize_window()          # 最大化窗口
        # 调用登陆
        self.login()                             # 先登录再说
        self.driver.refresh()                    # 刷新页面
        self.status = 2                          # 登录成功标识
        print("###登录成功###")

    def isElementExist(self, element):
        flag = True
        browser = self.driver
        try:
            browser.find_element_by_xpath(element)
            return flag

        except:
            flag = False
            return flag

    def choose_ticket(self):
        if self.status == 2:                  #登录成功入口
            print("="*30)
            print("###开始进行日期及票价选择###")
            sleep(10)
            self.driver.find_element_by_class_name('buy-link').click()
            # while self.driver.title.find('确认订单') == -1:           # 如果跳转到了订单结算界面就算这步成功了，否则继续执行此步
            #     try:
            #         buybutton = self.driver.find_element_by_class_name('buybtn').text
            #         if buybutton == "提交缺货登记":
            #             # 改变现有状态
            #             self.status=2
            #             self.driver.get(target_url)
            #             print('###抢票未开始，刷新等待开始###')
            #             continue
            #         elif buybutton == "立即预定":
            #             self.driver.find_element_by_class_name('buybtn').click()
            #             # 改变现有状态
            #             self.status = 3
            #         elif buybutton == "立即购买":
            #             self.driver.find_element_by_class_name('buybtn').click()
            #             # 改变现有状态
            #             self.status = 4
            #         # 选座购买暂时无法完成自动化
            #         elif buybutton == "选座购买":
            #             self.driver.find_element_by_class_name('buybtn').click()
            #             self.status = 5
            #     except:
            #         print('###未跳转到订单结算界面###')
            #     title = self.driver.title
            #     if title == '选座购买':
            #         # 实现选座位购买的逻辑
            #         self.choice_seats()
            #     elif title == '确认订单':
            #         while True:
            #             # 如果标题为确认订单
            #             print('waiting ......')
            #             if self.isElementExist('//*[@id="container"]/div/div[9]/button'):
            #                 self.check_order()
            #                 break

    def choice_seats(self):
        while self.driver.title == '选座购买':
            while self.isElementExist('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/img'):
                # 座位手动选择 选中座位之后//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/img 就会消失
                print('请快速的选择您的座位！！！')
            # 消失之后就会出现 //*[@id="app"]/div[2]/div[2]/div[2]/div
            while self.isElementExist('//*[@id="app"]/div[2]/div[2]/div[2]/div'):
                # 找到之后进行点击确认选座
                self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[2]/button').click()

    def check_order(self):
        if self.status in [3,4,5]:
            print('###开始确认订单###')
            try:
                # 默认选第一个购票人信息
                self.driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[2]/div[1]/div/label').click()
            except Exception as e:
                print("###购票人信息选中失败，自行查看元素位置###")
                print(e)
            # 最后一步提交订单
            time.sleep(0.5)  # 太快会影响加载，导致按钮点击无效
            self.driver.find_element_by_xpath('//div[@class = "w1200"]//div[2]//div//div[9]//button[1]').click()


    def finish(self):
        self.driver.quit()


if __name__ == '__main__':
    print('begin')
    try:
        print('try')
        con = JD()                  # 具体如果填写请查看类中的初始化函数
        con.enter_jd()              # 打开浏览器
        con.choose_ticket()         # 开始抢票

    except Exception as e:
        print(e)
        #con.finish()


# # 启动火狐浏览器的驱动器
# driver = webdriver.Firefox()
# # 最大化浏览器
# driver.maximize_window()
#
#
# # 传入用户名密码，登录淘宝
# def login():
#     # 打开淘宝
#     driver.get("https://www.jd.com/")
#
#     # 查找文本，登录
#     if driver.find_element_by_link_text("亲，请登录"):
#         driver.find_element_by_link_text("亲，请登录").click()
#
#     print("请在30秒内完成扫码")
#     time.sleep(30)
#
#     driver.get("https://cart.taobao.com/cart.htm")
#     time.sleep(3)
#
#     # 点击购物车里全选按钮
#     if driver.find_element_by_id("J_SelectAll1"):
#         driver.find_element_by_id("J_SelectAll1").click()
#     time.sleep(3)
#     now = datetime.datetime.now()
#     print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))
#
#
# def buy(buytime):
#     while True:
#         now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         if now == buytime:
#             try:
#                 # 点击结算按钮
#                 if driver.find_element_by_id("J_Go"):
#                     driver.find_element_by_id("J_Go").click()
#                     print("结算成功")
#                     submit()
#             except:
#                 pass
#         print(now)
#         time.sleep(0.01)
#
#
# def submit():
#     while True:
#         try:
#             if driver.find_element_by_link_text('提交订单'):
#                 driver.find_element_by_link_text('提交订单').click()
#                 now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
#                 print("抢购成功时间：%s" % now1)
#                 break
#         except:
#             print("再次尝试提交订单")
#             time.sleep(0.01)
#
#
# if __name__ == "__main__":
#     # 登录
#     login()
#     # 设置抢购时间
#     buy('2022-02-16 09:34:00')