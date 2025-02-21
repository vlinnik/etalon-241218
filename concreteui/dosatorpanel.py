#!/usr/bin/python3
# -*- coding: utf-8 -*-

from AnyQt.QtCore import QSize,QCoreApplication,Qt,QMetaObject,Property
from AnyQt.QtWidgets import QGroupBox,QApplication,QGridLayout,QLabel
from numbers import Number

class _Ui_DosatorPanel(object):
    def setupUi(self, panel):
        if not panel.objectName():
            panel.setObjectName(u"DosatorPanel")
        panel.resize(140, 60)
        panel.setStyleSheet(u"QLabel[style=\"weight\"]\n"
"{\n"
"	font-size: 20pt;\n"
"	font-weight: bold;\n"
"}\n"
"QLabel:disabled[style=\"target\"]\n"
"{\n"
"	font-size: 18pt;\n"
"	font-weight: bold;\n"
"	color: purple;\n"
"}\n"
"QLabel[style=\"small\"]\n"
"{\n"
"	font-size: 9pt;\n"
"}\n"
"QGroupBox\n"
"{\n"
"	border-radius: 4px;\n"
"	border: 1px solid red;\n"
"	background-color: rgba(255, 255, 255, 191);\n"
"	font-size: 7pt;\n"
"	font-weight: bold;\n"
"}\n"
" QGroupBox::title {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top center; /* position at the top center */\n"
"     padding: 0px 3px;\n"
"	background: none;\n"
"}\n"
"")
        panel.setAlignment(Qt.AlignCenter)
        self.gridLayout = QGridLayout(panel)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, -1, 0, 5)
        self.weight = QLabel(panel)
        self.weight.setObjectName(u"weight")
        self.weight.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.weight, 0, 0, 1, 1)


        self.retranslateUi(panel)

        QMetaObject.connectSlotsByName(panel)
    # setupUi

    def retranslateUi(self, panel):
        panel.setWindowTitle(QCoreApplication.translate("DosatorPanel", u"DosatorPanel", None))
        panel.setTitle(QCoreApplication.translate("DosatorPanel", u"\u0414\u041e\u0417\u0410\u0422\u041e\u0420", None))
        self.weight.setText(QCoreApplication.translate("DosatorPanel", u"0000", None))
        self.weight.setProperty("style", QCoreApplication.translate("DosatorPanel", u"weight", None))
    # retranslateUi


class DosatorPanel(QGroupBox):
    def __init__(self, parent=None):
        super(DosatorPanel, self).__init__(parent)
        self._ui = _Ui_DosatorPanel( )
        self._w = None
        self._precision = 0
        self._ui.setupUi(self)
        
    def setWeight(self,w: float ):
        self._w = w
        if isinstance(w,Number):
            self._ui.weight.setText( ('{:04'+f'.{self._precision}'+'f}').format(w) )
    
    def getWeight(self)->float:
        return self._w
    
    def setPrecision(self,p):
        self._precision = p
        self.setWeight(self._w)
    
    def getPrecision(self)->int:
        return self._precision

    def sizeHint(self):
        return QSize(140, 60)

    weight = Property(float,getWeight,setWeight)
    precision = Property(int,getPrecision,setPrecision)

if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    panel = DosatorPanel()
    panel.show()
    sys.exit(app.exec())
