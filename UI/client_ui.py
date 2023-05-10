# Form implementation generated from reading ui file 'UI/client_v2.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DataExForm(object):
    def setupUi(self, DataExForm):
        DataExForm.setObjectName("DataExForm")
        DataExForm.resize(751, 503)
        DataExForm.setStyleSheet("QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 rgb(222, 233, 255), stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 2ex; /* leave space at the top for the title */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    border: 1px solid grey;\n"
"    padding: 0 3px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #aaaaff, stop: 1 #FFFFFF);\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 1px solid grey;\n"
"    border-radius: 3px;\n"
"    background-color:rgba(170, 170, 255, 50);\n"
"    padding: 3px;\n"
"}\n"
"QPushButton:pressed {\n"
"    border-color: black;\n"
"    background-color:rgba(170, 170, 255, 100);\n"
"}\n"
"QPushButton:hover {\n"
"    border-color: black;\n"
"}")
        self.dataRecordBox = QtWidgets.QGroupBox(parent=DataExForm)
        self.dataRecordBox.setGeometry(QtCore.QRect(10, 250, 291, 241))
        self.dataRecordBox.setStyleSheet("")
        self.dataRecordBox.setObjectName("dataRecordBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dataRecordBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nameLabel = QtWidgets.QLabel(parent=self.dataRecordBox)
        self.nameLabel.setObjectName("nameLabel")
        self.verticalLayout.addWidget(self.nameLabel)
        self.nameEdit = QtWidgets.QLineEdit(parent=self.dataRecordBox)
        self.nameEdit.setObjectName("nameEdit")
        self.verticalLayout.addWidget(self.nameEdit)
        self.expLabel = QtWidgets.QLabel(parent=self.dataRecordBox)
        self.expLabel.setObjectName("expLabel")
        self.verticalLayout.addWidget(self.expLabel)
        self.expSpin = QtWidgets.QSpinBox(parent=self.dataRecordBox)
        self.expSpin.setProperty("value", 5)
        self.expSpin.setObjectName("expSpin")
        self.verticalLayout.addWidget(self.expSpin)
        self.birthLabel = QtWidgets.QLabel(parent=self.dataRecordBox)
        self.birthLabel.setObjectName("birthLabel")
        self.verticalLayout.addWidget(self.birthLabel)
        self.birthEdit = QtWidgets.QDateEdit(parent=self.dataRecordBox)
        self.birthEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(1995, 5, 13), QtCore.QTime(0, 0, 0)))
        self.birthEdit.setObjectName("birthEdit")
        self.verticalLayout.addWidget(self.birthEdit)
        self.sendRecordButton = QtWidgets.QPushButton(parent=self.dataRecordBox)
        self.sendRecordButton.setStyleSheet("")
        self.sendRecordButton.setObjectName("sendRecordButton")
        self.verticalLayout.addWidget(self.sendRecordButton)
        self.textGroup = QtWidgets.QGroupBox(parent=DataExForm)
        self.textGroup.setGeometry(QtCore.QRect(10, 140, 291, 101))
        self.textGroup.setObjectName("textGroup")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.textGroup)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit = QtWidgets.QLineEdit(parent=self.textGroup)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.sendTextButton = QtWidgets.QPushButton(parent=self.textGroup)
        self.sendTextButton.setObjectName("sendTextButton")
        self.verticalLayout_2.addWidget(self.sendTextButton)
        self.imageGroup = QtWidgets.QGroupBox(parent=DataExForm)
        self.imageGroup.setGeometry(QtCore.QRect(310, 20, 431, 471))
        self.imageGroup.setStyleSheet("")
        self.imageGroup.setFlat(False)
        self.imageGroup.setCheckable(False)
        self.imageGroup.setObjectName("imageGroup")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.imageGroup)
        self.gridLayout_2.setContentsMargins(-1, 3, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.sendImageButton = QtWidgets.QPushButton(parent=self.imageGroup)
        self.sendImageButton.setObjectName("sendImageButton")
        self.gridLayout_2.addWidget(self.sendImageButton, 0, 2, 1, 1)
        self.imagePathEdit = QtWidgets.QLineEdit(parent=self.imageGroup)
        self.imagePathEdit.setObjectName("imagePathEdit")
        self.gridLayout_2.addWidget(self.imagePathEdit, 0, 0, 1, 1)
        self.imagePathButton = QtWidgets.QPushButton(parent=self.imageGroup)
        self.imagePathButton.setObjectName("imagePathButton")
        self.gridLayout_2.addWidget(self.imagePathButton, 0, 1, 1, 1)
        self.imageLabel = QtWidgets.QLabel(parent=self.imageGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setMaximumSize(QtCore.QSize(400, 400))
        self.imageLabel.setText("")
        self.imageLabel.setPixmap(QtGui.QPixmap("UI\\img.bmp"))
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setObjectName("imageLabel")
        self.gridLayout_2.addWidget(self.imageLabel, 1, 0, 1, 3)
        self.methodGroup = QtWidgets.QGroupBox(parent=DataExForm)
        self.methodGroup.setGeometry(QtCore.QRect(10, 20, 291, 111))
        self.methodGroup.setObjectName("methodGroup")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.methodGroup)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listWidget = QtWidgets.QListWidget(parent=self.methodGroup)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout_3.addWidget(self.listWidget)

        self.retranslateUi(DataExForm)
        self.listWidget.setCurrentRow(0)
        QtCore.QMetaObject.connectSlotsByName(DataExForm)

    def retranslateUi(self, DataExForm):
        _translate = QtCore.QCoreApplication.translate
        DataExForm.setWindowTitle(_translate("DataExForm", "DataExchange"))
        self.dataRecordBox.setTitle(_translate("DataExForm", "Запись/Структура"))
        self.nameLabel.setText(_translate("DataExForm", "Имя"))
        self.nameEdit.setText(_translate("DataExForm", "Иван Иванов"))
        self.expLabel.setText(_translate("DataExForm", "Стаж"))
        self.birthLabel.setText(_translate("DataExForm", "Дата Рождения"))
        self.sendRecordButton.setText(_translate("DataExForm", "Отправить"))
        self.textGroup.setTitle(_translate("DataExForm", "Текст"))
        self.textEdit.setText(_translate("DataExForm", "Какой-то текст"))
        self.sendTextButton.setText(_translate("DataExForm", "Отправить"))
        self.imageGroup.setTitle(_translate("DataExForm", "Изображение"))
        self.sendImageButton.setText(_translate("DataExForm", "Отправить"))
        self.imagePathEdit.setText(_translate("DataExForm", "UI\\img.bpm"))
        self.imagePathButton.setText(_translate("DataExForm", "Поиск"))
        self.methodGroup.setTitle(_translate("DataExForm", "Метод"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("DataExForm", "Clipboard"))
        item = self.listWidget.item(1)
        item.setText(_translate("DataExForm", "Socket"))
        item = self.listWidget.item(2)
        item.setText(_translate("DataExForm", "Copydata"))
        self.listWidget.setSortingEnabled(__sortingEnabled)