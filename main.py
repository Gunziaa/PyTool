# -*- coding: utf-8 -*-
import sys
from PySide6.QtGui import QPainter, Qt, QGuiApplication, QMouseEvent
from PySide6.QtWidgets import QApplication

from ui.ToolUI import MyTool

from src.window.subTool import Tool
from src.window.systemTray import SystemTray


class MyMain(MyTool, SystemTray):

    def __init__(self):
        super().__init__()

        self.setAttribute(Qt.WA_DeleteOnClose, True)

        self.tray_icon()  # 托盘图标

        # 主窗口设置
        screen = QGuiApplication.primaryScreen().geometry()  # 获取屏幕类并调用geometry()方法获取屏幕大小
        self.screen_width = screen.width()  # 获取屏幕的宽 x
        self.screen_height = screen.height()  # 获取屏幕的高 y

        # 动画开关
        self.start_animation()

        # self.initAnimation()  # main初始化动画

        # 初始化鼠标位置
        self.mouse_press_pos = None
        self.mouse_move = False

    def passs(self):  # 托盘菜单 按钮调用的函数
        print('没做好')

    def paintEvent(self, event):
        # 绘制透明背景
        painter = QPainter(self)
        painter.fillRect(event.rect(), Qt.transparent)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.mouse_press_pos = event.pos()

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            if self.mouse_press_pos and not self.mouse_move:
                self.LeftBtuttonClicked()

            self.mouse_move = False
            self.mouse_press_pos = None

        elif event.button() == Qt.RightButton:
            self.RighButtinClicked()

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if event.buttons() == Qt.LeftButton:
            self.mouse_move = True
            delta = event.pos() - self.mouse_press_pos
            self.move(self.pos() + delta)

    def a(self):

        print(self.pos())

    # 单击左键
    def LeftBtuttonClicked(self):
        self.a()
        print('单击左键')

    # 双击左键
    def LeftDoubleButtonClicked(self):
        print('双击左键')

    # 单击右键
    def RighButtinClicked(self):
        t.StartTool(self.screen_width, self.screen_height, self.pos())

    # 双击右键
    def RighDoubleButtonClicked(self):
        print('双击右键')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MyMain()
    t = Tool()
    main_window.show()
    sys.exit(app.exec())
