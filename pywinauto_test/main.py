# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from pywinauto.application import Application
from time import sleep

# # 启动
app = Application(backend="uia").start(r"D:\Program Files (x86)\Foxit Software\Foxit Reader Plus\FoxitReaderPlus.exe")
print(app)
sleep(3)

# # 连接已启动的程序
# # 进程号连接
# app = Application(backend="uia").connect(process=21368)
# print(app)

# # 窗口句柄连接
# app = Application(backend="uia").connect(handle=200270)
# print(app)

# 窗口选择
# 方式1 app[类名/标题]
# 使用类名选择窗口
# dlg = app["classFoxitReaderPlus"]
# print(dlg)

# 使用标题选择窗口
dlg = app["开始 - 福昕阅读器专业版"]
print(dlg)

# 方式2 app.窗口类名
# dlg = app.SunAwtFrame
# print(dlg)

# dlg.print_control_identifiers()

# 窗口最大化
# dlg.maximize()
# sleep(3)
#
# # 窗口最小化
# dlg.minimize()
# sleep(3)
#
# # 恢复
# dlg.restore()
# sleep(3)
#
# status = dlg.get_show_state()
# print(status)

# 选择控件
# 方式1
# menu = dlg.Toolbar
# menu.print_control_identifiers()

# 方式2
menu = dlg["Pane5"].child_window(title="Quick Access Toolbar", control_type="ToolBar")
# menu.print_control_identifiers()

# ---------可能报错---------------
# 选择控件的子控件
# menu = dlg["Toolbar"][打开]
# menu.print_control_identifiers()

# 方式3
open = menu.child_window(title="打开", control_type="Button")
# open.print_control_identifiers()


# 子窗口 Spy++ 显示有这个窗口 但打不开 奇怪
# childwd = app["BCGPRibbonBar:ec0000:8:10003:10"]
# childwd.print_control_identifiers()


# 查看控件类型
# print(dlg.wrapper_object())
# print(menu.wrapper_object())
# print(open.wrapper_object())

# 查看对象支持的的方法
# print(dir(dlg.wrapper_object()))
# print(dir(menu.wrapper_object()))
# print(dir(open.wrapper_object()))

# 控件的文本内容获取
print(dlg.texts())

# 获取子元素
print(dlg.children())
print(menu.children())









dlg.close()