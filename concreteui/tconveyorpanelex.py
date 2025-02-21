# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TConveyorPanel.ui'
##
## Created by: Qt User Interface Compiler version 5.15.13
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from AnyQt.QtCore import *  # type: ignore
from AnyQt.QtGui import *  # type: ignore
from AnyQt.QtWidgets import *  # type: ignore

try:
    from . import tconveyorpanel_rc
except:
    import tconveyorpanel_rc

class Ui_TConveyorPanelEx(object):
    def setupUi(self, TConveyorPanelEx):
        if not TConveyorPanelEx.objectName():
            TConveyorPanelEx.setObjectName(u"TConveyorPanelEx")
        TConveyorPanelEx.resize(224, 194)
        TConveyorPanelEx.setStyleSheet(u"QGroupBox\n"
"{\n"
"	background-color: rgba(59, 59, 59,164);\n"
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
"QPushButton:flat\n"
"{\n"
"	border: 1px solid gray;\n"
"	border-radius: 4px;\n"
"	color: lightGray;\n"
"}\n"
"QPushButton:flat:hover\n"
"{\n"
"	background-color: gray;\n"
"}\n"
"QPushButton:flat:pressed:hover,QPushButton:flat:checked:hover,QPushButton:flat:checked\n"
"{\n"
"	background-color: green;\n"
"}\n"
"#more\n"
"{\n"
"	color: lightGray;\n"
""
                        "	font-size: 9pt;\n"
"	border: none;\n"
"	background: none;\n"
"}\n"
"#more::indicator:unchecked \n"
"{\n"
"	image: url(:/TConveyorPanel/more.png);\n"
"	width: 24px;\n"
"}\n"
"#more::indicator:checked \n"
"{\n"
"	image: url(:/TConveyorPanel/less.png);\n"
"	width: 24px;\n"
"}")
        TConveyorPanelEx.setAlignment(Qt.AlignCenter)
        self.verticalLayout = QVBoxLayout(TConveyorPanelEx)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(-1, 24, -1, -1)
        self.ctl_group = QWidget(TConveyorPanelEx)
        self.ctl_group.setObjectName(u"ctl_group")
        self.ctl_group.setMinimumSize(QSize(184, 36))
        self.ctl_group.setMaximumSize(QSize(184, 36))
        self.power = QPushButton(self.ctl_group)
        self.power.setObjectName(u"power")
        self.power.setGeometry(QRect(9, 2, 171, 32))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.power.sizePolicy().hasHeightForWidth())
        self.power.setSizePolicy(sizePolicy)
        self.power.setMinimumSize(QSize(160, 32))
        self.power.setMaximumSize(QSize(16777215, 32))
        self.power.setCursor(QCursor(Qt.PointingHandCursor))
        self.power.setCheckable(True)
        self.power.setFlat(True)
        self.powered = QLabel(self.ctl_group)
        self.powered.setObjectName(u"powered")
        self.powered.setGeometry(QRect(23, 11, 16, 16))
        self.powered.setMinimumSize(QSize(16, 16))
        self.powered.setMaximumSize(QSize(16, 16))
        self.powered.setPixmap(QPixmap(u":/TConveyorPanel/bolt.png"))
        self.powered.setScaledContents(True)
        self.powered.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.ctl_group)

        self.more = QCheckBox(TConveyorPanelEx)
        self.more.setObjectName(u"more")
        self.more.setCursor(QCursor(Qt.PointingHandCursor))
        self.more.setChecked(True)

        self.verticalLayout.addWidget(self.more)

        self.preferences = QWidget(TConveyorPanelEx)
        self.preferences.setObjectName(u"preferences")
        self.gridLayout = QGridLayout(self.preferences)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.hint_2 = QLabel(self.preferences)
        self.hint_2.setObjectName(u"hint_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.hint_2.sizePolicy().hasHeightForWidth())
        self.hint_2.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.hint_2, 1, 0, 1, 1)

        self.stopT = QSpinBox(self.preferences)
        self.stopT.setObjectName(u"stopT")
        self.stopT.setAlignment(Qt.AlignCenter)
        self.stopT.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout.addWidget(self.stopT, 0, 2, 1, 1)

        self.hint_1 = QLabel(self.preferences)
        self.hint_1.setObjectName(u"hint_1")
        sizePolicy1.setHeightForWidth(self.hint_1.sizePolicy().hasHeightForWidth())
        self.hint_1.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.hint_1, 0, 0, 1, 1)

        self.active = QCheckBox(self.preferences)
        self.active.setObjectName(u"active")

        self.gridLayout.addWidget(self.active, 1, 2, 1, 1, Qt.AlignHCenter)

        self.hint_3 = QLabel(self.preferences)
        self.hint_3.setObjectName(u"hint_3")
        sizePolicy1.setHeightForWidth(self.hint_3.sizePolicy().hasHeightForWidth())
        self.hint_3.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.hint_3, 2, 0, 1, 1)

        self.active_2 = QCheckBox(self.preferences)
        self.active_2.setObjectName(u"active_2")

        self.gridLayout.addWidget(self.active_2, 2, 2, 1, 1, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.preferences)


        self.retranslateUi(TConveyorPanelEx)
        self.more.toggled.connect(self.preferences.setVisible)

        QMetaObject.connectSlotsByName(TConveyorPanelEx)
    # setupUi

    def retranslateUi(self, TConveyorPanelEx):
        TConveyorPanelEx.setWindowTitle(QCoreApplication.translate("TConveyorPanelEx", u"\u041d\u0430\u043a\u043b\u043e\u043d\u043d\u044b\u0439 \u043a\u043e\u043d\u0432\u0435\u0439\u0435\u0440", None))
        TConveyorPanelEx.setTitle(QCoreApplication.translate("TConveyorPanelEx", u"\u041a\u043e\u043d\u0432\u0435\u0439\u0435\u0440 \u0432\u044b\u0433\u0440\u0443\u0437\u043a\u0438", None))
        self.power.setText(QCoreApplication.translate("TConveyorPanelEx", u"\u0412\u041a\u041b\u042e\u0427\u0418\u0422\u042c", None))
        self.powered.setText("")
        self.more.setText(QCoreApplication.translate("TConveyorPanelEx", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c", None))
        self.hint_2.setText(QCoreApplication.translate("TConveyorPanelEx", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442:", None))
        self.stopT.setSuffix(QCoreApplication.translate("TConveyorPanelEx", u" \u0441\u0435\u043a", None))
        self.hint_1.setText(QCoreApplication.translate("TConveyorPanelEx", u"T \u043e\u0442\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f:", None))
        self.active.setText("")
        self.hint_3.setText(QCoreApplication.translate("TConveyorPanelEx", u"\u0420\u0435\u0432\u0435\u0440\u0441:", None))
        self.active_2.setText("")
    # retranslateUi

class TConveyorPanelEx(QGroupBox):
    def __init__(self, *args, **kwargs):
        super(QGroupBox, self).__init__(*args, **kwargs)
        self._ui = Ui_TConveyorPanelEx()
        self._ui.setupUi(self)
        self._ui.more.setChecked(False)

if __name__ == "__main__":
        import sys

        app = QApplication(sys.argv)
        panel = TConveyorPanelEx()
        panel.show()
        sys.exit(app.exec())
    