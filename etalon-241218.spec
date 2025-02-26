# -*- mode: python ; coding: utf-8 -*-

import os
from AnyQt.QtCore import QLibraryInfo

datas = [ ('default.scada','.'),('ui','./ui'),('resources','./resources'),('SCADA.rcc','.'),('concrete6.dat','.') ]
binaries = [
    (os.path.join(QLibraryInfo.location(QLibraryInfo.LibraryLocation.PluginsPath), 'SCADA/modules', 'libconcrete6.so'), 'PyQt5/Qt5/plugins/SCADA/modules'),
    (os.path.join(QLibraryInfo.location(QLibraryInfo.LibraryLocation.PluginsPath), 'sqldrivers', 'libqsqlmysql.so'), 'PyQt5/Qt5/plugins/sqldrivers'),
    (os.path.join(QLibraryInfo.location(QLibraryInfo.LibraryLocation.LibraryExecutablesPath), 'QtWebEngineProcess'), 'PyQt5/Qt5/libexec'),
]

a = Analysis(
    ['gui/__main__.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=["SCADA_qrc","concreteui.dosatorpanel","concreteui.doserpanel","concreteui.tconveyorpanel","concreteui.tconveyorpanelex","concreteui.mixerpanel","concreteui.mcontainerpanel","animation","runtimetrend",'AnyQt.QtSql','AnyQt.QtWebEngineWidgets'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PyQt6','PySide2'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='etalon-241218',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['resources/power.png'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='etalon-241218',
)
