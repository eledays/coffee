# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.refreshBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.refreshBtn.setGeometry(QtCore.QRect(10, 510, 80, 23))
        self.refreshBtn.setObjectName("refreshBtn")
        self.table = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 10, 791, 491))
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.editBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.editBtn.setGeometry(QtCore.QRect(100, 510, 161, 23))
        self.editBtn.setObjectName("editBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.refreshBtn.setText(_translate("MainWindow", "Обновить"))
        self.editBtn.setText(_translate("MainWindow", "Добавить/изменить"))
