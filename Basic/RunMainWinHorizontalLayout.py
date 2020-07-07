import sys
import MainWinHorizontalLayout
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':  # 只有直接运行脚本 才会执行这个条件句
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = MainWinHorizontalLayout.Ui_MainWindow()
    # 在主窗口上添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
