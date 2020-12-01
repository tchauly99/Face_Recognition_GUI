# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Form1.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1066, 847)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(100, 70, 811, 531))
        self.tabWidget.setObjectName("tabWidget")
        self.Dlib = QtWidgets.QWidget()
        self.Dlib.setObjectName("Dlib")
        self.ListUser_Cb = QtWidgets.QComboBox(self.Dlib)
        self.ListUser_Cb.setGeometry(QtCore.QRect(250, 400, 141, 21))
        self.ListUser_Cb.setObjectName("ListUser_Cb")
        self.Start_Btn = QtWidgets.QPushButton(self.Dlib)
        self.Start_Btn.setGeometry(QtCore.QRect(40, 430, 75, 23))
        self.Start_Btn.setObjectName("Start_Btn")
        self.Capture_Btn = QtWidgets.QPushButton(self.Dlib)
        self.Capture_Btn.setGeometry(QtCore.QRect(40, 400, 75, 23))
        self.Capture_Btn.setObjectName("Capture_Btn")
        self.Lock_Lb = QtWidgets.QLabel(self.Dlib)
        self.Lock_Lb.setGeometry(QtCore.QRect(210, 430, 51, 21))
        self.Lock_Lb.setFrameShape(QtWidgets.QFrame.Panel)
        self.Lock_Lb.setTextFormat(QtCore.Qt.AutoText)
        self.Lock_Lb.setIndent(0)
        self.Lock_Lb.setObjectName("Lock_Lb")
        self.Stop_Btn = QtWidgets.QPushButton(self.Dlib)
        self.Stop_Btn.setGeometry(QtCore.QRect(120, 430, 75, 23))
        self.Stop_Btn.setObjectName("Stop_Btn")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Dlib)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 501, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Player = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Player.setAutoFillBackground(False)
        self.Player.setStyleSheet("border: 2px solid black")
        self.Player.setScaledContents(True)
        self.Player.setAlignment(QtCore.Qt.AlignCenter)
        self.Player.setWordWrap(False)
        self.Player.setObjectName("Player")
        self.horizontalLayout.addWidget(self.Player)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.username_Tb = QtWidgets.QLineEdit(self.Dlib)
        self.username_Tb.setGeometry(QtCore.QRect(130, 400, 113, 20))
        self.username_Tb.setObjectName("username_Tb")
        self.horizontalSlider = QtWidgets.QSlider(self.Dlib)
        self.horizontalSlider.setGeometry(QtCore.QRect(80, 360, 371, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.LeftTimeLabel = QtWidgets.QLabel(self.Dlib)
        self.LeftTimeLabel.setGeometry(QtCore.QRect(480, 360, 47, 13))
        self.LeftTimeLabel.setObjectName("LeftTimeLabel")
        self.PlayButton = QtWidgets.QPushButton(self.Dlib)
        self.PlayButton.setGeometry(QtCore.QRect(40, 350, 31, 31))
        self.PlayButton.setText("")
        self.PlayButton.setObjectName("PlayButton")
        self.DeleteUser_Btn = QtWidgets.QPushButton(self.Dlib)
        self.DeleteUser_Btn.setGeometry(QtCore.QRect(400, 400, 75, 23))
        self.DeleteUser_Btn.setObjectName("DeleteUser_Btn")
        self.tabWidget.addTab(self.Dlib, "")
        self.Manual = QtWidgets.QWidget()
        self.Manual.setObjectName("Manual")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.Manual)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(160, 380, 371, 16))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.LeftTimeLabel_2 = QtWidgets.QLabel(self.Manual)
        self.LeftTimeLabel_2.setGeometry(QtCore.QRect(560, 380, 47, 13))
        self.LeftTimeLabel_2.setObjectName("LeftTimeLabel_2")
        self.ListUser_Cb_3 = QtWidgets.QComboBox(self.Manual)
        self.ListUser_Cb_3.setGeometry(QtCore.QRect(340, 420, 141, 21))
        self.ListUser_Cb_3.setObjectName("ListUser_Cb_3")
        self.Stop_Btn_2 = QtWidgets.QPushButton(self.Manual)
        self.Stop_Btn_2.setGeometry(QtCore.QRect(430, 450, 71, 31))
        self.Stop_Btn_2.setObjectName("Stop_Btn_2")
        self.Start_Btn_2 = QtWidgets.QPushButton(self.Manual)
        self.Start_Btn_2.setGeometry(QtCore.QRect(340, 450, 81, 31))
        self.Start_Btn_2.setObjectName("Start_Btn_2")
        self.Capture_Btn_3 = QtWidgets.QPushButton(self.Manual)
        self.Capture_Btn_3.setGeometry(QtCore.QRect(120, 420, 75, 23))
        self.Capture_Btn_3.setObjectName("Capture_Btn_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Manual)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(120, 40, 501, 331))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Player_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Player_2.setAutoFillBackground(False)
        self.Player_2.setStyleSheet("border: 2px solid black")
        self.Player_2.setScaledContents(True)
        self.Player_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Player_2.setWordWrap(False)
        self.Player_2.setObjectName("Player_2")
        self.horizontalLayout_2.addWidget(self.Player_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.DeleteUser_Btn_3 = QtWidgets.QPushButton(self.Manual)
        self.DeleteUser_Btn_3.setGeometry(QtCore.QRect(490, 420, 75, 23))
        self.DeleteUser_Btn_3.setObjectName("DeleteUser_Btn_3")
        self.username_Tb_3 = QtWidgets.QLineEdit(self.Manual)
        self.username_Tb_3.setGeometry(QtCore.QRect(220, 420, 113, 20))
        self.username_Tb_3.setObjectName("username_Tb_3")
        self.PlayButton_2 = QtWidgets.QPushButton(self.Manual)
        self.PlayButton_2.setGeometry(QtCore.QRect(120, 370, 31, 31))
        self.PlayButton_2.setText("")
        self.PlayButton_2.setObjectName("PlayButton_2")
        self.Lock_Lb_2 = QtWidgets.QLabel(self.Manual)
        self.Lock_Lb_2.setGeometry(QtCore.QRect(510, 450, 41, 31))
        self.Lock_Lb_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.Lock_Lb_2.setObjectName("Lock_Lb_2")
        self.Gen_Btn_3 = QtWidgets.QPushButton(self.Manual)
        self.Gen_Btn_3.setGeometry(QtCore.QRect(120, 450, 93, 28))
        self.Gen_Btn_3.setObjectName("Gen_Btn_3")
        self.Train_Btn = QtWidgets.QPushButton(self.Manual)
        self.Train_Btn.setGeometry(QtCore.QRect(230, 450, 93, 28))
        self.Train_Btn.setObjectName("Train_Btn")
        self.tabWidget.addTab(self.Manual, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1066, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionSave_file = QtWidgets.QAction(MainWindow)
        self.actionSave_file.setObjectName("actionSave_file")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionOpen_File_2 = QtWidgets.QAction(MainWindow)
        self.actionOpen_File_2.setObjectName("actionOpen_File_2")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionZoom_in = QtWidgets.QAction(MainWindow)
        self.actionZoom_in.setObjectName("actionZoom_in")
        self.actionZoom_out = QtWidgets.QAction(MainWindow)
        self.actionZoom_out.setObjectName("actionZoom_out")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.menuFile.addAction(self.actionOpen_File_2)
        self.menuFile.addAction(self.actionExit_2)
        self.menuView.addAction(self.actionZoom_in)
        self.menuView.addAction(self.actionZoom_out)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionDelete)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Start_Btn.setText(_translate("MainWindow", "Start"))
        self.Capture_Btn.setText(_translate("MainWindow", "Capture"))
        self.Lock_Lb.setText(_translate("MainWindow", "  Locked"))
        self.Stop_Btn.setText(_translate("MainWindow", "Stop"))
        self.Player.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">Player</span></p></body></html>"))
        self.username_Tb.setText(_translate("MainWindow", "Chau"))
        self.LeftTimeLabel.setText(_translate("MainWindow", "TextLabel"))
        self.DeleteUser_Btn.setText(_translate("MainWindow", "Delete User"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Dlib), _translate("MainWindow", "Dlib"))
        self.LeftTimeLabel_2.setText(_translate("MainWindow", "TextLabel"))
        self.Stop_Btn_2.setText(_translate("MainWindow", "Stop"))
        self.Start_Btn_2.setText(_translate("MainWindow", "Start"))
        self.Capture_Btn_3.setText(_translate("MainWindow", "Capture"))
        self.Player_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">Player</span></p></body></html>"))
        self.DeleteUser_Btn_3.setText(_translate("MainWindow", "Delete User"))
        self.username_Tb_3.setText(_translate("MainWindow", "Chau"))
        self.Lock_Lb_2.setText(_translate("MainWindow", "Locked"))
        self.Gen_Btn_3.setText(_translate("MainWindow", "Generate"))
        self.Train_Btn.setText(_translate("MainWindow", "Train Model"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Manual), _translate("MainWindow", "Manual"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionSave_file.setText(_translate("MainWindow", "Save file"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionOpen_File_2.setText(_translate("MainWindow", "Open File"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))
        self.actionZoom_in.setText(_translate("MainWindow", "Zoom in"))
        self.actionZoom_out.setText(_translate("MainWindow", "Zoom out"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
