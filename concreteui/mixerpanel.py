# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MixerPanel.ui'
##
## Created by: Qt User Interface Compiler version 5.15.13
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

try:
        from AnyQt.QtCore import Q_FLAGS as Q_ENUM
except:
        from AnyQt.QtCore import  pyqtEnum as Q_ENUM
        
from AnyQt.QtCore import *  # type: ignore
from AnyQt.QtGui import *  # type: ignore
from AnyQt.QtWidgets import *  # type: ignore

from enum import Enum
from . import mixerpanel_rc

class __Ui_MixerPanel(object):
    def setupUi(self, panel):
        if not panel.objectName():
            panel.setObjectName(u"MixerPanel")
        panel.resize(292, 73)
        panel.setStyleSheet(u"QGroupBox\n"
"{\n"
"	margin-top: 2ex;\n"
"	color: white;\n"
"	font-weight: bold;\n"
"	font-size: 10pt;\n"
"	background: none;\n"
"	border: 1px solid red;\n"
"}\n"
"QGroupBox::title \n"
"{\n"
"     subcontrol-origin: margin;\n"
"     subcontrol-position: top center; /* position at the top center */\n"
"     padding: 0 3px;\n"
" }\n"
"QToolButton\n"
"{\n"
"	border: 1px solid gray;\n"
"	border-radius: 4px;\n"
"}\n"
"QToolButton:checked, QToolButton:pressed\n"
"{\n"
"	background: green;\n"
"}\n"
"QToolButton:!checked:hover\n"
"{\n"
"	background: lightGray;	\n"
"}\n"
"QToolButton:checked:hover\n"
"{\n"
"	background: darkGreen;	\n"
"}")
        panel.setAlignment(Qt.AlignCenter)
        self.horizontalLayout = QHBoxLayout(panel)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.open = QToolButton(panel)
        self.open.setObjectName(u"open")
        self.open.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/MixerPanel/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open.setIcon(icon)
        self.open.setIconSize(QSize(32, 32))
        self.open.setCheckable(True)

        self.horizontalLayout.addWidget(self.open)

        self.close = QToolButton(panel)
        self.close.setObjectName(u"close")
        self.close.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/MixerPanel/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close.setIcon(icon1)
        self.close.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.close)

        self.ack = QToolButton(panel)
        self.ack.setObjectName(u"ack")
        self.ack.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/MixerPanel/enable.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ack.setIcon(icon2)
        self.ack.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.ack)

        self.nack = QToolButton(panel)
        self.nack.setObjectName(u"nack")
        self.nack.setCursor(QCursor(Qt.PointingHandCursor))
        self.nack.setStyleSheet(u"\u0417\u0430\u043f\u0440\u0435\u0442\u0438\u0442\u044c \u0432\u044b\u0433\u0440\u0443\u0437\u043a\u0443")
        icon3 = QIcon()
        icon3.addFile(u":/MixerPanel/disable.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nack.setIcon(icon3)
        self.nack.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.nack)

        self.lock = QToolButton(panel)
        self.lock.setObjectName(u"lock")
        self.lock.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/MixerPanel/unlocked.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/MixerPanel/locked.png", QSize(), QIcon.Normal, QIcon.On)
        self.lock.setIcon(icon4)
        self.lock.setIconSize(QSize(32, 32))
        self.lock.setCheckable(True)

        self.horizontalLayout.addWidget(self.lock)

        self.manual = QToolButton(panel)
        self.manual.setObjectName(u"manual")
        self.manual.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/MixerPanel/wheel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.manual.setIcon(icon5)
        self.manual.setIconSize(QSize(32, 32))
        self.manual.setCheckable(True)

        self.horizontalLayout.addWidget(self.manual)


        self.retranslateUi(panel)

        QMetaObject.connectSlotsByName(panel)
    # setupUi

    def retranslateUi(self, panel):
        panel.setWindowTitle(QCoreApplication.translate("MixerPanel", u"MixerPanel", None))
        panel.setTitle(QCoreApplication.translate("MixerPanel", u"\u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u0442\u0432\u043e\u0440\u043e\u043c", None))
#if QT_CONFIG(tooltip)
        self.open.setToolTip(QCoreApplication.translate("MixerPanel", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c/\u0437\u0430\u043a\u0440\u044b\u0442\u044c \u0441\u043c\u0435\u0441\u0438\u0442\u0435\u043b\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.open.setText(QCoreApplication.translate("MixerPanel", u"O", None))
#if QT_CONFIG(tooltip)
        self.close.setToolTip(QCoreApplication.translate("MixerPanel", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c/\u0437\u0430\u043a\u0440\u044b\u0442\u044c \u0441\u043c\u0435\u0441\u0438\u0442\u0435\u043b\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.close.setText(QCoreApplication.translate("MixerPanel", u"O", None))
#if QT_CONFIG(tooltip)
        self.ack.setToolTip(QCoreApplication.translate("MixerPanel", u"\u0420\u0430\u0437\u0440\u0435\u0448\u0438\u0442\u044c \u0432\u044b\u0433\u0440\u0443\u0437\u043a\u0443", None))
#endif // QT_CONFIG(tooltip)
        self.ack.setText(QCoreApplication.translate("MixerPanel", u"A", None))
#if QT_CONFIG(shortcut)
        self.ack.setShortcut(QCoreApplication.translate("MixerPanel", u"F2", None))
#endif // QT_CONFIG(shortcut)
        self.nack.setText(QCoreApplication.translate("MixerPanel", u"N", None))
#if QT_CONFIG(tooltip)
        self.lock.setToolTip(QCoreApplication.translate("MixerPanel", u"\u0411\u043b\u043e\u043a\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0437\u0430\u0442\u0432\u043e\u0440", None))
#endif // QT_CONFIG(tooltip)
        self.lock.setText(QCoreApplication.translate("MixerPanel", u"L", None))
#if QT_CONFIG(tooltip)
        self.manual.setToolTip(QCoreApplication.translate("MixerPanel", u"\u0420\u0443\u0447\u043d\u043e\u0435 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.manual.setText(QCoreApplication.translate("MixerPanel", u"M", None))
    # retranslateUi

class GateTypes(Enum):
        Pneumatic = 1
        Hydraulic = 0

class MixerPanel(QGroupBox,__Ui_MixerPanel):
        GateTypes = GateTypes
        Q_ENUM(GateTypes)
        
        Pneumatic = GateTypes.Pneumatic
        Hydraulic = GateTypes.Hydraulic

        def __init__(self, *args, **kwargs):
                super(QGroupBox, self).__init__(*args, **kwargs)
                self.setupUi(self)
                self.setGateType(GateTypes.Pneumatic)
                
        def setGateType(self,_type: GateTypes):
                self._gateType = _type
                if _type==1:
                        self.open.setCheckable(True)
                        self.close.setVisible(False)
                else:
                        self.open.setCheckable(False)
                        self.close.setVisible(True)
                
        def getGateType(self)->GateTypes:
                return self._gateType
        
        gateType = Property(GateTypes,getGateType,setGateType)

if __name__ == "__main__":
        import sys

        app = QApplication(sys.argv)
        panel = MixerPanel()
        panel.show()
        sys.exit(app.exec())
