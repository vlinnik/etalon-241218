# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ElevatorPanel.ui'
##
## Created by: Qt User Interface Compiler version 5.15.13
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from AnyQt.QtCore import *  # type: ignore
from AnyQt.QtGui import *  # type: ignore
from AnyQt.QtWidgets import *  # type: ignore

from . import elevatorpanel_rc

class __Ui_ElevatorPanel(object):
    def setupUi(self, panel):
        if not panel.objectName():
            panel.setObjectName(u"ElevatorPanel")
        panel.resize(264, 354)
        panel.setStyleSheet(u"QGroupBox\n"
"{\n"
"	background-color: rgba(59, 59, 59,120);\n"
"	color: gray;\n"
"	border: 1px solid red;\n"
"	border-radius: 4px;\n"
"	font-size: 9pt;\n"
"	color: lightGray;\n"
"}\n"
"QGroupBox QLabel\n"
"{\n"
"	color: lightGray;\n"
"	font-size: 10pt;\n"
"}\n"
"QLabel:enabled[style=\"alarm\"]\n"
"{\n"
"	border: 1px solid red;\n"
"	border-radius: 4px;\n"
"	background-color: rgba(255,0,0,100);\n"
"	padding: 4px;\n"
"	color: white;\n"
"	font-weight: bold;\n"
"}\n"
"QLabel:disabled[style=\"alarm\"]\n"
"{\n"
"	border: 1px solid gray;\n"
"	border-radius: 4px;\n"
"	background-color: rgba(0,0,0,100);\n"
"	padding: 4px;\n"
"	color: darkGray;\n"
"	font-weight: bold;\n"
"}\n"
"QToolButton{\n"
"	background: none;\n"
"	border: 1px solid gray;\n"
"	border-radius: 4px;\n"
"}\n"
"QCheckBox\n"
"{\n"
"	color: lightGray;\n"
"	font-size: 9pt;\n"
"	border: none;\n"
"	background: none;\n"
"}\n"
"QCheckBox::indicator:unchecked \n"
"{\n"
"	image: url(:/ElevatorPanel/more.png);\n"
"	width: 24px;\n"
"}\n"
"QCheckBox::indicator:checke"
                        "d \n"
"{\n"
"	image: url(:/ElevatorPanel/less.png);\n"
"	width: 24px;\n"
"}\n"
"QCommandLinkButton\n"
"{\n"
"	border: 1px solid gray;\n"
"	border-radius: 4px;\n"
"	color: lightGray;\n"
"}\n"
"QCommandLinkButton:hover\n"
"{\n"
"	background-color: gray;\n"
"}\n"
"QCommandLinkButton:pressed:hover,QCommandLinkButton:checked\n"
"{\n"
"	background-color: green;\n"
"}")
        panel.setAlignment(Qt.AlignCenter)
        self.verticalLayout_2 = QVBoxLayout(panel)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout_2.setContentsMargins(-1, 24, -1, 5)
        self.fault = QLabel(panel)
        self.fault.setObjectName(u"fault")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fault.sizePolicy().hasHeightForWidth())
        self.fault.setSizePolicy(sizePolicy)
        self.fault.setAlignment(Qt.AlignCenter)
        self.fault.setProperty("style", u"alarm")

        self.verticalLayout_2.addWidget(self.fault)

        self.center = QWidget(panel)
        self.center.setObjectName(u"center")
        self.gridLayout = QGridLayout(self.center)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.commandUp = QCommandLinkButton(self.center)
        self.commandUp.setObjectName(u"commandUp")
        self.commandUp.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/ElevatorPanel/moveup.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandUp.setIcon(icon)

        self.gridLayout.addWidget(self.commandUp, 0, 0, 1, 1)

        self.rightSide = QWidget(self.center)
        self.rightSide.setObjectName(u"rightSide")
        self.verticalLayout = QVBoxLayout(self.rightSide)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.statusUp = QLabel(self.rightSide)
        self.statusUp.setObjectName(u"statusUp")
        self.statusUp.setPixmap(QPixmap(u":/ElevatorPanel/moveup.png"))
        self.statusUp.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.statusUp)

        self.toolButton = QToolButton(self.rightSide)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/ElevatorPanel/clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.toolButton, 0, Qt.AlignHCenter)

        self.statusDown = QLabel(self.rightSide)
        self.statusDown.setObjectName(u"statusDown")
        self.statusDown.setPixmap(QPixmap(u":/ElevatorPanel/movedown.png"))
        self.statusDown.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.statusDown)


        self.gridLayout.addWidget(self.rightSide, 0, 1, 3, 1)

        self.commandStop = QCommandLinkButton(self.center)
        self.commandStop.setObjectName(u"commandStop")
        self.commandStop.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/ElevatorPanel/disable.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandStop.setIcon(icon2)
        self.commandStop.setCheckable(True)

        self.gridLayout.addWidget(self.commandStop, 1, 0, 1, 1)

        self.commandDown = QCommandLinkButton(self.center)
        self.commandDown.setObjectName(u"commandDown")
        self.commandDown.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/ElevatorPanel/movedown.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandDown.setIcon(icon3)

        self.gridLayout.addWidget(self.commandDown, 2, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.center)

        self.group_footer = QWidget(panel)
        self.group_footer.setObjectName(u"group_footer")
        self.horizontalLayout = QHBoxLayout(self.group_footer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.more = QCheckBox(self.group_footer)
        self.more.setObjectName(u"more")
        self.more.setCursor(QCursor(Qt.PointingHandCursor))
        self.more.setChecked(True)

        self.horizontalLayout.addWidget(self.more)


        self.verticalLayout_2.addWidget(self.group_footer)

        self.group_timings = QWidget(panel)
        self.group_timings.setObjectName(u"group_timings")
        self.formLayout = QFormLayout(self.group_timings)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.group_timings)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.unloadT = QSpinBox(self.group_timings)
        self.unloadT.setObjectName(u"unloadT")
        self.unloadT.setAlignment(Qt.AlignCenter)
        self.unloadT.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.unloadT)

        self.label_8 = QLabel(self.group_timings)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.maxMoveT = QSpinBox(self.group_timings)
        self.maxMoveT.setObjectName(u"maxMoveT")
        self.maxMoveT.setAlignment(Qt.AlignCenter)
        self.maxMoveT.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.maxMoveT)

        self.label_11 = QLabel(self.group_timings)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_11)

        self.maxMoveT_2 = QSpinBox(self.group_timings)
        self.maxMoveT_2.setObjectName(u"maxMoveT_2")
        self.maxMoveT_2.setAlignment(Qt.AlignCenter)
        self.maxMoveT_2.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.maxMoveT_2)

        self.label_12 = QLabel(self.group_timings)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_12)

        self.maxMoveT_3 = QSpinBox(self.group_timings)
        self.maxMoveT_3.setObjectName(u"maxMoveT_3")
        self.maxMoveT_3.setAlignment(Qt.AlignCenter)
        self.maxMoveT_3.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.maxMoveT_3)


        self.verticalLayout_2.addWidget(self.group_timings)


        self.retranslateUi(panel)
        self.more.toggled.connect(self.group_timings.setVisible)

        QMetaObject.connectSlotsByName(panel)
    # setupUi

    def retranslateUi(self, ElevatorPanel):
        ElevatorPanel.setWindowTitle(QCoreApplication.translate("ElevatorPanel", u"ElevatorPanel", None))
        ElevatorPanel.setTitle(QCoreApplication.translate("ElevatorPanel", u"\u0421\u041a\u0418\u041f", None))
        self.fault.setText(QCoreApplication.translate("ElevatorPanel", u"\u0410\u0412\u0410\u0420\u0418\u042f", None))
        self.commandUp.setText(QCoreApplication.translate("ElevatorPanel", u"\u041f\u043e\u0434\u043d\u044f\u0442\u044c", None))
        self.commandUp.setDescription(QCoreApplication.translate("ElevatorPanel", u"\u0432\u0432\u0435\u0440\u0445", None))
        self.statusUp.setText("")
        self.toolButton.setText(QCoreApplication.translate("ElevatorPanel", u"R", None))
        self.statusDown.setText("")
        self.commandStop.setText(QCoreApplication.translate("ElevatorPanel", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.commandStop.setDescription(QCoreApplication.translate("ElevatorPanel", u"\u0410\u0432\u0430\u0440\u0438\u044f", None))
        self.commandDown.setText(QCoreApplication.translate("ElevatorPanel", u"\u041e\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
        self.commandDown.setDescription(QCoreApplication.translate("ElevatorPanel", u"\u0432\u043d\u0438\u0437", None))
        self.more.setText(QCoreApplication.translate("ElevatorPanel", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c", None))
        self.label_6.setText(QCoreApplication.translate("ElevatorPanel", u"T \u0432\u044b\u0433\u0440\u0443\u0437\u043a\u0438:", None))
        self.unloadT.setSuffix(QCoreApplication.translate("ElevatorPanel", u" \u0441\u0435\u043a", None))
        self.label_8.setText(QCoreApplication.translate("ElevatorPanel", u"<html><head/><body><p>T<span style=\" vertical-align:sub;\">\u043c\u0430\u043a\u0441</span> \u0445\u043e\u0434\u0430:</p></body></html>", None))
        self.maxMoveT.setSuffix(QCoreApplication.translate("ElevatorPanel", u" \u0441\u0435\u043a", None))
        self.label_11.setText(QCoreApplication.translate("ElevatorPanel", u"<html><head/><body><p>T<span style=\" vertical-align:sub;\">\u043f\u0430\u0443\u0437\u0430</span> \u043f\u043e\u0434\u044a\u0435\u043c\u0430:</p></body></html>", None))
        self.maxMoveT_2.setSuffix(QCoreApplication.translate("ElevatorPanel", u" \u0441\u0435\u043a", None))
        self.label_12.setText(QCoreApplication.translate("ElevatorPanel", u"<html><head/><body><p>T<span style=\" vertical-align:sub;\">\u043f\u0440\u0435\u0434</span> \u043f\u043e\u0434\u044a\u0435\u043c\u0430:</p></body></html>", None))
        self.maxMoveT_3.setSuffix(QCoreApplication.translate("ElevatorPanel", u" \u0441\u0435\u043a", None))
    # retranslateUi

class ElevatorPanel(QGroupBox,__Ui_ElevatorPanel):
        def __init__(self, *args, **kwargs):
                super(QGroupBox, self).__init__(*args, **kwargs)
                self.setupUi(self)

if __name__ == "__main__":
        import sys

        app = QApplication(sys.argv)
        panel = ElevatorPanel()
        panel.show()
        sys.exit(app.exec())
