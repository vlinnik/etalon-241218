# Сборка pyinstaller

## Создание spec файла

```
$ pyi-makespec  --windowed --icon=resources/power.png --name=etalon-241218 --exclude PyQt6 --exclude PySide2 __main__.py
        --hidden-import=qwt
        --hidden-import=AnyQt.QtSql
        --hidden-import=SCADA_qrc
        --hidden-import=animation
        --hidden-import=runtimetrend
        --hidden-import=concreteui.dosatorpanel
        --hidden-import=concreteui.doserpanel
        --hidden-import=concreteui.tconveyorpanel
        --hidden-import=concreteui.tconveyorpanelex
        --hidden-import=concreteui.mixerpanel
        --hidden-import=concreteui.mcontainerpanel
```
### Дополнительно в spec

АСУ БСУ зависит от необходимых файлов и бинарников, которые надо добавить вручную

```
import os
from AnyQt.QtCore import QLibraryInfo

datas = [ ('default.scada','.'),('ui','./ui'),('resources','./resources'),('SCADA.rcc','.'),('concrete6.dat','.') ]
binaries = [
    (os.path.join(QLibraryInfo.location(QLibraryInfo.LibraryLocation.PluginsPath), 'SCADA/modules', 'libconcrete6.so'), 'PyQt5/Qt5/plugins/SCADA/modules'),
    (os.path.join(QLibraryInfo.location(QLibraryInfo.LibraryLocation.PluginsPath), 'sqldrivers', 'libqsqlmysql.so'), 'PyQt5/Qt5/plugins/sqldrivers'),
]
```

в секции 

```
a = Analysis(...)
```

изменить параметры binaries и datas

# Кастомные Widget на python

Home.ui использует Widgets, которые сделаны на python-е. Чтобы стали доступны в панели нужно

Из каталога проекта (где файлы *plugin.py)

```
PYQTDESIGNERPATH=. designer
```

в designer должен быть установлен libpyqt5/libpyqt5 