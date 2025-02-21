#!/usr/bin/python3

from AnyQt.QtGui import QIcon
from AnyQt.QtDesigner import QPyDesignerCustomWidgetPlugin

from concreteui.tconveyorpanelex import TConveyorPanelEx
from concreteui.tconveyorpanel import TConveyorPanel
from concreteui.dosatorpanel import DosatorPanel
from concreteui.doserpanel import DoserPanel
from concreteui.mixerpanel import MixerPanel
import concreteui.tconveyorpanel_rc

class __TConveyorPanelExPlugin(QPyDesignerCustomWidgetPlugin):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return TConveyorPanelEx(parent)

    def name(self):
        return "TConveyorPanelEx"

    def group(self):
        return "PYSCA"

    def includeFile(self):
        return "concreteui.tconveyorpanelex"

    def icon(self):
        return QIcon()

    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""
    
    def isContainer(self):
        return False

class __TConveyorPanelPlugin(QPyDesignerCustomWidgetPlugin):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return TConveyorPanel(parent)

    def name(self):
        return "TConveyorPanel"

    def group(self):
        return "PYSCA"

    def includeFile(self):
        return "concreteui.tconveyorpanel"

    def icon(self):
        return QIcon()

    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""
    
    def isContainer(self):
        return False

class __DosatorPanelPlugin(QPyDesignerCustomWidgetPlugin):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return DosatorPanel(parent)

    def name(self):
        return "DosatorPanel"

    def group(self):
        return "PYSCA"

    def includeFile(self):
        return "concreteui.dosatorpanel"

    def icon(self):
        return QIcon()

    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""
    
    def isContainer(self):
        return False

class __DoserPanelPlugin(QPyDesignerCustomWidgetPlugin):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return DoserPanel(parent)

    def name(self):
        return "DoserPanel"

    def group(self):
        return "PYSCA"

    def includeFile(self):
        return "concreteui.doserpanel"

    def icon(self):
        return QIcon()

    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""
    
    def isContainer(self):
        return False

class __MixerPanelPlugin(QPyDesignerCustomWidgetPlugin):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return MixerPanel(parent)

    def name(self):
        return "MixerPanel"

    def group(self):
        return "PYSCA"

    def includeFile(self):
        return "concreteui.mixerpanel"

    def icon(self):
        return QIcon()

    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""
    
    def isContainer(self):
        return False