import os,sys
if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

from pysca import app,PYPLC

try:
    from  . import navbar
    from .concrete6 import concrete6
except:
    import navbar
    from concrete6 import concrete6

from AnyQt.QtWidgets import QApplication
from AnyQt.QtGui import QIcon

# import subprocess
# logic = subprocess.Popen(["python", "src/krax.py"])

def make_tooltip(*args):
    try:
        n = 0
        msg = '<table><tr><th align="left">КОМПОНЕНТ</th><th align="right">M</th></tr>'
        for arg in args:
            if arg>0:
                msg += f'<tr><td>{concrete6.containers[n].component}</td><td align="right">{arg:.0f}</td></tr>\n'
            n+=1
        msg+='</table>'
        return msg
    except:
        pass
    
    return "Here should be an tooltip"

def main():
    Home = app.window('ui/Home.ui',ctx={"make_tooltip":make_tooltip})

    navbar.append( Home )
    navbar.tools( app.window('ui/Extensions.ui'))

    concrete6.setContainerPanels( [Home.cpanel_0,Home.cpanel_1,Home.cpanel_2,Home.cpanel_4,Home.cpanel_3,Home.cpanel_5,Home.cpanel_6,Home.cpanel_7] )
    concrete6.setMainWindow(navbar.instance)
    app.object(concrete6.instance)

    navbar.instance.setWindowTitle(Home.windowTitle())
    navbar.instance.setWindowIcon(Home.windowIcon())
    navbar.instance.show( )
            
    dev = PYPLC('192.168.2.10')
    app.devices['${PLC}'] = dev
    dev.start(100)

    app.start( ctx = globals() )

    dev.stop( )

    concrete6.cleanup( )

# logic.terminate( )

if __name__=='__main__':
    main( )