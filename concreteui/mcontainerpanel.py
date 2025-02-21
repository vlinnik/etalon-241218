# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MContainerPanel.ui'
##
## Created by: Qt User Interface Compiler version 5.15.13
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from AnyQt.QtCore import *  # type: ignore
from AnyQt.QtGui import *  # type: ignore
from AnyQt.QtWidgets import QGroupBox,QLabel,QPushButton,QGridLayout,QVBoxLayout,QLayout,QWidget,QSizePolicy,QCheckBox,QSpacerItem,QSpinBox,QAbstractSpinBox,QApplication  # type: ignore

from . import mcontainerpanel_rc

class _Ui_MContainerPanel(object):
    def setupUi(self, MContainerPanel):
        if not MContainerPanel.objectName():
            MContainerPanel.setObjectName(u"MContainerPanel")
        MContainerPanel.resize(224, 158)
        MContainerPanel.setStyleSheet(u"QGroupBox\n"
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
"	image: url(:/MContainerPanel/more.png);\n"
"	width: 24px;\n"
"}\n"
"#more::indicator:checked \n"
"{\n"
"	image: url(:/MContainerPanel/less.png);\n"
"	width: 24px;\n"
"}")
        MContainerPanel.setAlignment(Qt.AlignCenter)
        self.verticalLayout = QVBoxLayout(MContainerPanel)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(-1, 24, -1, -1)
        self.ctl_group = QWidget(MContainerPanel)
        self.ctl_group.setObjectName(u"ctl_group")
        self.ctl_group.setMinimumSize(QSize(184, 36))
        self.ctl_group.setMaximumSize(QSize(184, 36))
        self.open = QPushButton(self.ctl_group)
        self.open.setObjectName(u"open")
        self.open.setGeometry(QRect(9, 2, 171, 32))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open.sizePolicy().hasHeightForWidth())
        self.open.setSizePolicy(sizePolicy)
        self.open.setMinimumSize(QSize(160, 32))
        self.open.setMaximumSize(QSize(16777215, 32))
        self.open.setCursor(QCursor(Qt.PointingHandCursor))
        self.open.setCheckable(True)
        self.open.setFlat(True)
        self.powered = QLabel(self.ctl_group)
        self.powered.setObjectName(u"powered")
        self.powered.setGeometry(QRect(23, 11, 16, 16))
        self.powered.setMinimumSize(QSize(16, 16))
        self.powered.setMaximumSize(QSize(16, 16))
        self.powered.setPixmap(QPixmap(u":/MContainerPanel/bolt.png"))
        self.powered.setScaledContents(True)
        self.powered.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.ctl_group)

        self.more = QCheckBox(MContainerPanel)
        self.more.setObjectName(u"more")
        self.more.setCursor(QCursor(Qt.PointingHandCursor))
        self.more.setChecked(True)

        self.verticalLayout.addWidget(self.more)

        self.preferences = QWidget(MContainerPanel)
        self.preferences.setObjectName(u"preferences")
        self.gridLayout = QGridLayout(self.preferences)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.stopT = QSpinBox(self.preferences)
        self.stopT.setObjectName(u"stopT")
        self.stopT.setAlignment(Qt.AlignCenter)
        self.stopT.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout.addWidget(self.stopT, 0, 2, 1, 1)

        self.hint_2 = QLabel(self.preferences)
        self.hint_2.setObjectName(u"hint_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.hint_2.sizePolicy().hasHeightForWidth())
        self.hint_2.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.hint_2, 1, 0, 1, 1)

        self.hint_1 = QLabel(self.preferences)
        self.hint_1.setObjectName(u"hint_1")
        sizePolicy1.setHeightForWidth(self.hint_1.sizePolicy().hasHeightForWidth())
        self.hint_1.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.hint_1, 0, 0, 1, 1)

        self.active = QCheckBox(self.preferences)
        self.active.setObjectName(u"active")

        self.gridLayout.addWidget(self.active, 1, 2, 1, 1, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.preferences)


        self.retranslateUi(MContainerPanel)
        self.more.toggled.connect(self.preferences.setVisible)

        QMetaObject.connectSlotsByName(MContainerPanel)
    # setupUi

    def retranslateUi(self, MContainerPanel):
        MContainerPanel.setWindowTitle(QCoreApplication.translate("MContainerPanel", u"\u041f\u0440\u043e\u043c\u0435\u0436\u0443\u0442\u043e\u0447\u043d\u044b\u0439 \u0431\u0443\u043d\u043a\u0435\u0440", None))
        MContainerPanel.setTitle(QCoreApplication.translate("MContainerPanel", u"\u041f\u0440\u043e\u043c\u0435\u0436\u0443\u0442\u043e\u0447\u043d\u044b\u0439 \u0431\u0443\u043d\u043a\u0435\u0440", None))
        self.open.setText(QCoreApplication.translate("MContainerPanel", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.powered.setText("")
        self.more.setText(QCoreApplication.translate("MContainerPanel", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c", None))
        self.stopT.setSuffix(QCoreApplication.translate("MContainerPanel", u" \u0441\u0435\u043a", None))
        self.hint_2.setText(QCoreApplication.translate("MContainerPanel", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442:", None))
        self.hint_1.setText(QCoreApplication.translate("MContainerPanel", u"T \u0432\u044b\u0433\u0440\u0443\u0437\u043a\u0438:", None))
        self.active.setText("")
    # retranslateUi

class MContainerPanel(QGroupBox):
    
    def __init__(self, *args, **kwargs):
        super(QGroupBox, self).__init__(*args, **kwargs)
        self._ui = _Ui_MContainerPanel( )
        self._ui.setupUi(self)
        self._ui.more.setChecked(False)
                
if __name__ == "__main__":
        import sys

        app = QApplication(sys.argv)
        panel = MContainerPanel()
        panel.show()
        sys.exit(app.exec())
