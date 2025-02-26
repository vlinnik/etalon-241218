from typing import List
from AnyQt.QtCore import QPluginLoader,QLibraryInfo,QObject,Signal
from AnyQt.QtWidgets import QApplication,QMainWindow,QWidget
import os

class _Container():
    def __init__(self,target: QObject):
        self._target = target
    
    @property
    def component(self)->str:
        return self._target.property('component')

class _Proxy():
    """Класс-Обертка для загрузки модуля concrete6.
    """
    def __init__(self):
        path_hints = [QLibraryInfo.location(QLibraryInfo.LibraryLocation.PluginsPath)+'/SCADA/modules/libconcrete6.so','./modules/libconcrete6.so']
        plugin = QPluginLoader( QApplication.instance() )
        for p in path_hints:
            if os.path.exists(p):
                print(f'loading {os.path.abspath(p)}')
                plugin = QPluginLoader(os.path.abspath(p),QApplication.instance())
                break
        self._cp = []
        self._instance = None

        if plugin.load():
            self._instance = plugin.instance( )
            self._instance.reload( )
            self._instance.changed.connect(self._on_changed)
            self._instance.setProperty('defaults',False)
        else:
            print('failed to load concrete6 module',plugin.errorString())

        plugin.deleteLater( )

    def cleanup(self):
        self.instance.disconnect( )
        self.instance.save( )
        self.instance.deleteLater( )
        self._instance = None 
        
    def __del__(self):
        self.instance.save( )
        self.instance.deleteLater( )
        self._instance = None
    
    @property
    def instance(self)->QObject:
        return self._instance

    @property
    def containers(self)->List[_Container]:
        containers = []
        container = None
        index = 0
        while index==0 or container:
            container = self.instance.findChild(QObject,f"container_{index}")
            index+=1
            if container: containers.append(_Container(container))
        return containers
    
    def setMainWindow(self,w: QMainWindow):
        self.instance.setMainWindow(w)
        
    def save(self):
        self.instance.save()
        
    def reload(self):
        self.instance.reload()
        
    def containerPreferences(self,index: int):
        self.instance.containerPreferences(index)

    def dosatorPreferences(self,index: int):
        self.instance.dosatorPreferences(index)

    def mixerPreferences(self,index: int):
        self.instance.mixerPreferences(index)

    def _on_changed(self):
        for p in zip(self._cp,self.containers):
            p[0].component = p[1].component
        
    def setContainerPanels( self,panels: List[QWidget] ):
        self._cp = panels
        self._on_changed( )

    @property
    def changed(self)->Signal:
        return self.instance.changed
    
concrete6 = _Proxy( )