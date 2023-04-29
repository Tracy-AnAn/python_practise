# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# import win32api
# import win32gui
# import win32con
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# def find_idxSubHandle(pHandle, winClass, index=0):
#     """
#     已知子窗口的窗体类名
#     寻找第index号个同类型的兄弟窗口
#     """
#     assert type(index) == int and index >= 0
#     handle = win32gui.FindWindowEx(pHandle, 0, winClass, None)
#     while index > 0:
#         handle = win32gui.FindWindowEx(pHandle, handle, winClass, None)
#         index -= 1
#     return handle
#
#
# def find_subHandle(pHandle, winClassList):
#     """
#     递归寻找子窗口的句柄
#     pHandle是祖父窗口的句柄
#     winClassList是各个子窗口的class列表，父辈的list-index小于子辈
#     """
#     assert type(winClassList) == list
#     if len(winClassList) == 1:
#         return find_idxSubHandle(pHandle, winClassList[0][0], winClassList[0][1])
#     else:
#         pHandle = find_idxSubHandle(pHandle, winClassList[0][0], winClassList[0][1])
#         return find_subHandle(pHandle, winClassList[1:])
#
# class Qt5QWindowIcon(object):
#     def __init__(self, fgFilePath=None):
#         self.Mhandle = win32gui.FindWindow("Qt5QWindowIcon", "逍遥模拟器")            # 主窗口
#         self.Dhanlde = 0
#
#     def get_desk_wd(self):
#         tWindow = win32gui.FindWindowEx(self.Mhandle, 0, "Qt5QWindowIcon", "MainWindowWindow")
#         #print('%#x' % tWindow)
#         tWindow = win32gui.FindWindowEx(tWindow, 0, "Qt5QWindowIcon", "CenterWidgetWindow")
#         #print('%#x' % tWindow)
#         tWindow = win32gui.FindWindowEx(tWindow, 0, "Qt5QWindowIcon", "RenderWindowWindow")
#         #print('%#x' % tWindow)
#         tWindow = win32gui.FindWindowEx(tWindow, 0, "subWin", "sub")
#         #print('%#x' % tWindow)
#         self.Dhanlde = win32gui.FindWindowEx(tWindow, 0, "subWin", "sub")      # 手机桌面子窗口
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#     # 逍遥模拟器类
#     MainDw = Qt5QWindowIcon()       # 初始化对象
#     MainDw.get_desk_wd()            # 获取桌面句柄
#
#     print('%#x' % MainDw.Mhandle)
#     print('%#x' % MainDw.Dhanlde)
#
#     # 打开桌面上的京东APP
#     Menu = win32api.GetMenu(MainDw.Dhanlde)
#     print(Menu)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/


from pywinauto.application import Application
from time import sleep

# # 启动
# app = Application(backend="uia").start(r"D:\Program Files\Microvirt\MEmu\MEmu.exe")
# print(app)
# sleep(30)

# # 连接已启动的程序
# # 进程号连接
app = Application(backend="uia").connect(process=21368)
print(app)

# # 窗口句柄连接
# app = Application(backend="uia").connect(handle=200270)
# print(app)

# 窗口选择
# 方式1 app[类名/标题]
# 使用类名选择窗口
# dlg = app["classFoxitReaderPlus"]
# print(dlg)

# 使用标题选择窗口
dlg = app["逍遥模拟器"]
print(dlg)

# 方式2 app.窗口类名
# dlg = app.SunAwtFrame
# print(dlg)

dlg.print_control_identifiers()

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
menu = dlg.Toolbar
print(menu.print_control_identifiers())

# 方式2
menu = dlg["Toolbar"]
print(menu.print_control_identifiers())

dlg.close()


