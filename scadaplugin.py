#!/usr/bin/python3
from typing import List
from AnyQt.QtGui import QIcon
from AnyQt.QtWidgets import QWidget,QApplication
from AnyQt.QtDesigner import QPyDesignerCustomWidgetPlugin

from animation import Animation
from runtimetrend import RuntimeTrend

class __AnimationPlugin(QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return Animation(parent)

    def name(self):
        return "Animation"

    def group(self):
        return "PYSCA"

    def icon(self):
        return QIcon()

    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""

    def isContainer(self):
        return True

    def includeFile(self):
        return "animation"
    
class __RuntimeTrendPlugin(QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return RuntimeTrend(parent)

    def name(self):
        return "RuntimeTrend"

    def group(self):
        return "PYSCA"

    def icon(self):
        return QIcon()

    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""

    def isContainer(self):
        return False

    def includeFile(self):
        return "runtimetrend"
    
