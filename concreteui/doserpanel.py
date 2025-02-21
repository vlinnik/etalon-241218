#!/usr/bin/python3

from AnyQt.QtCore import QSize,QCoreApplication,Qt,QMetaObject,Property
from AnyQt.QtWidgets import QGroupBox,QApplication,QVBoxLayout,QLabel,QWidget,QHBoxLayout
from numbers import Number

class _Ui_DoserPanel:
    def setupUi(self, panel):
        if not panel.objectName():
            panel.setObjectName(u"container_0")
        panel.resize(130, 100)
        panel.setStyleSheet(u"QLabel[style=\"target\"]\n"
"{\n"
"	font-size: 18pt;\n"
"	font-weight: bold;\n"
"   color: black;\n"
"}\n"
"QWidget:enabled QLabel:enabled[style=\"target\"]\n"
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
"	font-size: 9pt;\n"
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
        self.verticalLayout = QVBoxLayout(panel)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 18, 0, 0)
        self.component = QLabel(panel)
        self.component.setObjectName(u"component")
        self.component.setAlignment(Qt.AlignCenter)
        self.component.setProperty("style", u"component")

        self.verticalLayout.addWidget(self.component)

        self.target = QLabel(panel)
        self.target.setObjectName(u"target")
        self.target.setAlignment(Qt.AlignCenter)
        self.target.setProperty("style", u"target")
        self.target.setEnabled(False)

        self.verticalLayout.addWidget(self.target)

        self.foorter = QWidget(panel)
        self.foorter.setObjectName(u"foorter")
        self.horizontalLayout = QHBoxLayout(self.foorter)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.error = QLabel(self.foorter)
        self.error.setObjectName(u"error")
        self.error.setAlignment(Qt.AlignCenter)
        self.error.setProperty("style", u"small")

        self.horizontalLayout.addWidget(self.error)

        self.expense = QLabel(self.foorter)
        self.expense.setObjectName(u"expense")
        self.expense.setAlignment(Qt.AlignCenter)
        self.expense.setProperty("style", u"small")

        self.horizontalLayout.addWidget(self.expense)


        self.verticalLayout.addWidget(self.foorter)


        self.retranslateUi(panel)

        QMetaObject.connectSlotsByName(panel)
    # setupUi

    def retranslateUi(self, panel):
        panel.setWindowTitle(QCoreApplication.translate("DoserPanel", u"DoserPanel", None))
        panel.setTitle(QCoreApplication.translate("DoserPanel", u"\u0411\u0423\u041d\u041a\u0415\u0420", None))
        self.component.setText(QCoreApplication.translate("DoserPanel", u"\u043a\u043e\u043c\u043f\u043e\u043d\u0435\u043d\u0442", None))
        self.target.setText(QCoreApplication.translate("DoserPanel", u"0000", None))
        self.error.setText(QCoreApplication.translate("DoserPanel", u"+0000 \u043a\u0433", None))
        self.expense.setText(QCoreApplication.translate("DoserPanel", u"+0000 \u043a\u0433", None))
    # retranslateUi

class DoserPanel(QGroupBox):
    def __init__(self, parent=None):
        super(DoserPanel, self).__init__(parent)
        self._precision = 0
        self._target = 0
        self._error = 0
        self._expense = 0
        self._busy = False
        self._ui = _Ui_DoserPanel()
        self._ui.setupUi(self)

    def sizeHint(self):
        return QSize(130, 100)

    def setPrecision(self,p):
        self._precision = p
        self.setTarget(self._target)
        self.setError(self._error)
        self.setExpense(self._expense)
    
    def getPrecision(self)->int:
        return self._precision
    
    def getComponent(self)->str:
        return self._ui.component.text()
    
    def setComponent(self,name: str):
        self._ui.component.setText(name)
    
    def getTarget(self)->float:
        return self._target
    
    def setTarget(self,sp: float ):
        if isinstance(sp,Number):
            self._target = sp
            self._ui.target.setText( ('{:04'+f'.{self._precision}'+'f}').format(sp) )
        
    def getError(self)->float:
        return self._error
    
    def setError(self,err: float ):
        if isinstance(err,Number):
            self._error = err
            self._ui.error.setText( ('{:+05'+f'.{self._precision}'+'f} кг').format(err) )
    
    def getExpense(self)->float:
        return self._expense
    
    def setExpense(self,q: float ):
        if isinstance(q,Number):
            self._expense = q
            self._ui.expense.setText( ('{:+05'+f'.{self._precision}'+'f} кг').format(q) )

    def getBusy(self)->bool:
        return self._busy

    def setBusy(self,b: bool):
        self._busy = b
        self._ui.target.setEnabled(b)
    
    component = Property(str,getComponent,setComponent)    
    busy = Property(bool,getBusy,setBusy)
    target = Property(float,getTarget,setTarget)
    expense = Property(float,getExpense,setExpense)
    error = Property(float,getError,setError)
    precision = Property(int,getPrecision,setPrecision)
                
if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    panel = DoserPanel()
    panel.show()
    sys.exit(app.exec())