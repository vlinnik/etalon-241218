from pyplc.config import plc
from project import name as project_name
from concrete.imitation import iMOTOR,iVALVE,iGATE,iWEIGHT,iROTARYFLOW
from concrete import Transport,Dosator,Weight,Container,Manager,Readiness,Loaded,Mixer,Factory,Lock
from concrete.msgate import MPGate,GRGate
from concrete.dosator import ManualDosator
from concrete.vibrator import Vibrator,UnloadHelper
from concrete.vodoley import Vodoley
from concrete.motor import MotorST
from concrete.container import Retarder
from pyplc.utils.misc import BLINK
from pyplc.utils.latch import RS
import sys

print(f'\tЗапуск проекта {project_name}')

factory_1 = Factory( )

cement_m_1 = Weight(raw = plc.CEMENT_M_1, mmax=1500)
silage_1 = Container( m = lambda: cement_m_1.m, out = plc.AUGER_ON_1, closed = ~plc.AUGER_ON_1,max_sp=1000,lock=Lock(key=lambda: not plc.DCEMENT_CLOSED_1 or plc.AUGER_ON_2))
silage_2 = Container( m =lambda: cement_m_1.m, out = plc.AUGER_ON_2, closed = ~plc.AUGER_ON_2,max_sp=1000,lock=Lock(key=lambda: not plc.DCEMENT_CLOSED_1 or plc.AUGER_ON_1))
cement_1 = Dosator( m = lambda: cement_m_1.m, closed = plc.DCEMENT_CLOSED_1, out = plc.DCEMENT_OPEN_1, containers=(silage_1,silage_2),lock=Lock(key=lambda: plc.AUGER_ON_1 or plc.AUGER_ON_2 ) )
dc_vibrator_1 = UnloadHelper( q = plc.DC_VIBRATOR_ON_1,dosator=cement_1,weight=cement_m_1, point = 30)

aerator_1 = BLINK(enable=plc.AUGER_ON_1,q = plc.AERATOR_ON_1 )
aerator_2 = BLINK(enable=plc.AUGER_ON_2,q = plc.AERATOR_ON_2 )
aerator_3 = BLINK(enable=plc.AUGER_ON_3,q = plc.AERATOR_ON_3 )

cement_m_2 = Weight(raw = plc.CEMENT_M_2, mmax=1500)
silage_3 = Container( m = lambda: cement_m_2.m, out = plc.AUGER_ON_3, closed = ~plc.AUGER_ON_3,max_sp=1000,lock=Lock(key=plc.DCEMENT_OPEN_2) )
cement_2 = Dosator( m = lambda:  cement_m_2.m, closed = plc.DCEMENT_CLOSED_2, out = plc.DCEMENT_OPEN_2, containers=(silage_3,),lock=Lock(key=plc.AUGER_ON_3) )
dc_vibrator_2 = UnloadHelper( q = plc.DC_VIBRATOR_ON_2,dosator=cement_2, weight= cement_m_2, point = 30)

# water_1   = FlowMeter( out=plc.WATER_OPEN_1, closed = ~plc.WATER_OPEN_1,clk=plc.WATER_CLK_1 )
water_1 = Vodoley(out = plc.WATER_OPEN_1, clk = plc.WATER_Q_1, humidity= plc.HUMIDITY_1 )

additions_m_1 = Weight(raw = plc.ADDITIONS_M_1,mmax=50)
addition_1 = Container( m = lambda:  additions_m_1.m,out = plc.APUMP_ON_1, closed = ~plc.APUMP_ON_1,max_sp=30,lock=Lock(key=plc.DADDITIONS_OPEN_1) )
additions_1 = Dosator(m = lambda:  additions_m_1.m, out=plc.DADDITIONS_OPEN_1, containers=(addition_1,),lock = Lock(key=plc.APUMP_ON_1) )

fillers_m_1 = Weight( raw = plc.CONVEYOR_M_1, mmax = 8000)
retarder_1 = Retarder( m=lambda:  fillers_m_1.m, outs=(plc.FILLER_OPEN_1,plc.FILLER_OPEN_2,plc.FILLER_OPEN_3),sts=(plc.FILLER_CLOSED_1,plc.FILLER_CLOSED_2,plc.FILLER_CLOSED_3)) 
filler_1 = Container(m = lambda:  fillers_m_1.m, out = retarder_1.out(0), closed=retarder_1.closed(0), lock = Lock(key=lambda: retarder_1.lock(0) or plc.CONVEYOR_ON_1 ), max_sp = 3000 )
filler_2 = Container(m = lambda:  fillers_m_1.m, out = retarder_1.out(1), closed=retarder_1.closed(1), lock = Lock(key=lambda: retarder_1.lock(1) or plc.CONVEYOR_ON_1 ), max_sp = 3000 )
filler_3 = Container(m = lambda:  fillers_m_1.m, out = retarder_1.out(2), closed=retarder_1.closed(2), lock = Lock(key=lambda: retarder_1.lock(2) or plc.CONVEYOR_ON_1 ), max_sp = 3000 )
vibrator_1 = Vibrator( q = plc.VIBRATOR_ON_1, containers = [plc.FILLER_OPEN_1], weight=fillers_m_1)
vibrator_2 = Vibrator( q = plc.VIBRATOR_ON_2, containers = [plc.FILLER_OPEN_2], weight=fillers_m_1)
vibrator_3 = Vibrator( q = plc.VIBRATOR_ON_3, containers = [plc.FILLER_OPEN_3], weight=fillers_m_1)

tconveyor_1 = Transport( ison = plc.TCONVEYOR_ISON_1, power = plc.TCONVEYOR_ON_1, out=plc.CONVEYOR_ON_1 )
conveyor_1 = Dosator( m= lambda: fillers_m_1.m, closed = ~plc.CONVEYOR_ON_1, out = tconveyor_1.set_auto, containers=(filler_1,filler_2,filler_3),lock=Lock(key=lambda: not plc.FILLER_CLOSED_1 or not plc.FILLER_CLOSED_2 or not plc.FILLER_CLOSED_3) )
mcontainer_1 = ManualDosator(level = plc.MCONTAINER_LEVEL_1, closed = plc.MCONTAINER_CLOSED_1,out = plc.MCONTAINER_OPEN_1, lock = ~plc.MIXER_ISON_1,dosator=conveyor_1, helper = plc.MC_VIBRATOR_ON_1 )

motor_1 = MotorST( ison=plc.MIXER_ISON_1,powered=plc.MIXER_ON_1,heat=7000)

def mixer_open_2(cmd: bool):
  plc.MIXER_OPEN_2 = cmd and not plc.MIXER_OPENED_2

def mixer_close_2(cmd: bool):
  plc.MIXER_CLOSE_2 = cmd and not plc.MIXER_CLOSED_2
  
def protect_gate_2():
  if plc.MIXER_CLOSED_2 and plc.MIXER_CLOSE_2:
    plc.MIXER_CLOSE_2 = False
  if plc.MIXER_OPENED_2 and plc.MIXER_OPEN_2:
    plc.MIXER_OPEN_2 = False
  
# историчиски сложилось что на заводе первый затвор это gate_2 тут...
gate_1 = MPGate( closed=plc.MIXER_CLOSED_1, opened=plc.MIXER_OPENED_1,close=plc.MIXER_CLOSE_1,open=plc.MIXER_OPEN_1)
gate_2 = MPGate( closed=plc.MIXER_CLOSED_2, opened=plc.MIXER_OPENED_2,close=mixer_close_2)
gates = GRGate(gates=[gate_1,gate_2])
mixer_1 = Mixer(gate = gates ,motor=motor_1, use_ack=False, flows=( c.q for c in (silage_1,silage_2,silage_3,water_1,addition_1)+ tuple(mcontainer_1.expenses) ))
gate_2.export("reverse",bool(False)) #добавим пользовательский атрибут включать реверс конвейера
water_1.install_counter( lambda: mixer_1.qreset )

def toggle_breakpoint(x:bool):
  mixer_1.breakpoint = x
  
forbid_1 = RS(set = ~plc.ALLOW_UNLOAD_1,reset=plc.ALLOW_UNLOAD_1,q = toggle_breakpoint )

loaded_2 = Loaded([cement_1,cement_2,additions_1,mcontainer_1])
water_1.join( 'go' , loaded_2 )

def power_tconveyor_2(on:bool):
  """Включение конвейера под смесителем зависит от того какой затвор выбран.

  Args:
      on (bool): комманда ВКЛЮЧИТЬ. 
  """
  if gate_2.reverse!=0: 
    plc.RCONVEYOR_ON_1 = on
    plc.FCONVEYOR_ON_1 = False
  else:
    plc.FCONVEYOR_ON_1 = on
    plc.RCONVEYOR_ON_1 = False

tconveyor_2 = Transport(ison=lambda: plc.RCONVEYOR_ISON_1 or plc.FCONVEYOR_ISON_1, power = power_tconveyor_2, out=mixer_open_2, hold_on=~plc.MIXER_CLOSED_2 )

def emergency(value: bool):
  if value:
    power_tconveyor_2(False)
    plc.MIXER_OPEN_2 = False
    plc.MIXER_OPEN_1 = False
    plc.MIXER_CLOSE_1= True
    plc.MIXER_CLOSE_2= True
    mixer_1.clock = 0
    
gate_2.bind('open',tconveyor_2.set_auto)

ready_1 = Readiness( (cement_1,cement_2,additions_1,mcontainer_1) )          #для замеса набрано все необходимое
loaded_1 = Loaded( (cement_1,cement_2,additions_1,mcontainer_1,water_1) )    #все необходимое загружено в смеситель
manager_1 = Manager(collected=ready_1,loaded = loaded_1, mixer = mixer_1, dosators=(cement_1,cement_2, additions_1, mcontainer_1) )

factory_1.on_mode = tuple(x.switch_mode for x in [conveyor_1,cement_1,cement_2,additions_1,mcontainer_1,conveyor_1,water_1])
factory_1.on_emergency = tuple(x.emergency for x in [conveyor_1,cement_1,cement_2,additions_1,mixer_1,mcontainer_1,water_1,manager_1,gate_1,gate_2,tconveyor_2] ) + (emergency,)
instances = ( mixer_1,cement_1, silage_1, silage_2, cement_2, silage_3, water_1, additions_1, addition_1, conveyor_1, 
             filler_1, filler_2, filler_3, tconveyor_1, mcontainer_1, cement_m_1, cement_m_2, additions_m_1, fillers_m_1,
             manager_1, factory_1, ready_1, loaded_1, vibrator_1, vibrator_2, vibrator_3, dc_vibrator_1, dc_vibrator_2, 
             aerator_1, aerator_2, aerator_3, forbid_1, protect_gate_2, motor_1, gate_1, gate_2, gates, tconveyor_2,retarder_1)

if sys.platform=='linux':
  imotor_1 = iMOTOR(simple = True, on = plc.MIXER_ON_1,ison = plc.MIXER_ISON_1)
  idcement_1 = iVALVE(open = plc.DCEMENT_OPEN_1, closed=plc.DCEMENT_CLOSED_1)
  idcement_2 = iVALVE(open = plc.DCEMENT_OPEN_2, closed=plc.DCEMENT_CLOSED_2)
  idadditions_1 = iVALVE(open = plc.DADDITIONS_OPEN_1,closed = plc.DADDITIONS_CLOSED_1)
  iauger_1 = iMOTOR(simple = True, on = plc.AUGER_ON_1,ison=plc.AUGER_ISON_1)  
  iauger_2 = iMOTOR(simple = True, on = plc.AUGER_ON_2,ison=plc.AUGER_ISON_2)
  iauger_3 = iMOTOR(simple = True, on = plc.AUGER_ON_3,ison=plc.AUGER_ISON_3)
  iapump_1 = iMOTOR(simple = True, on = plc.APUMP_ON_1,ison=plc.APUMP_ISON_1)
  iconveyor_1 = iMOTOR(simple = True,on = plc.CONVEYOR_ON_1,ison = plc.CONVEYOR_ISON_1)
  itconveyor_1 = iMOTOR(simple = True,on = plc.TCONVEYOR_ON_1,ison = plc.TCONVEYOR_ISON_1)
  ifiller_1 = iVALVE(open = plc.FILLER_OPEN_1,closed=plc.FILLER_CLOSED_1)
  ifiller_2 = iVALVE(open = plc.FILLER_OPEN_2,closed=plc.FILLER_CLOSED_2)
  ifiller_3 = iVALVE(open = plc.FILLER_OPEN_3,closed=plc.FILLER_CLOSED_3)
  igate_1 = iGATE(open = plc.MIXER_OPEN_1, close=plc.MIXER_CLOSE_1, closed = plc.MIXER_CLOSED_1,opened = plc.MIXER_OPENED_1)
  igate_2 = iGATE(open = plc.MIXER_OPEN_2, close=plc.MIXER_CLOSE_2, opened = plc.MIXER_OPENED_2,closed = plc.MIXER_CLOSED_2)
  
  icement_m_1 = iWEIGHT( loading=lambda: plc.AUGER_ON_1 or plc.AUGER_ON_2, unloading=plc.DCEMENT_OPEN_1, q = plc.CEMENT_M_1 ,speed=100)
  icement_m_2 = iWEIGHT( speed=30, loading=plc.AUGER_ON_3, unloading=plc.DCEMENT_OPEN_2, q = plc.CEMENT_M_2 )
  iadditions_m_1 = iWEIGHT(speed=50, loading = plc.APUMP_ON_1, unloading = plc.DADDITIONS_OPEN_1, q = plc.ADDITIONS_M_1 )
  ifillers_m_1 = iWEIGHT( speed=100,loading=lambda: plc.FILLER_OPEN_1 or plc.FILLER_OPEN_2 or plc.FILLER_OPEN_3,unloading=plc.CONVEYOR_ON_1, q = plc.CONVEYOR_M_1 )
  
  iwater_q_1 = iROTARYFLOW( loading=plc.WATER_OPEN_1, clk = plc.WATER_Q_1)
  
  irconveyor_2 = iMOTOR(simple=True,on = plc.RCONVEYOR_ON_1,ison = plc.RCONVEYOR_ISON_1 )
  ifconveyor_2 = iMOTOR(simple=True,on = plc.FCONVEYOR_ON_1,ison = plc.FCONVEYOR_ISON_1 )
  imcontainer_1 = iVALVE(open = plc.MCONTAINER_OPEN_1,closed = plc.MCONTAINER_CLOSED_1)
  ihumidity_1 = iWEIGHT( speed = 100,  loading = plc.WATER_OPEN_1, unloading=lambda: gates.unloading,q = plc.HUMIDITY_1 )
  
  imitations = ( imotor_1,idcement_1,idcement_2,idadditions_1,iauger_1,iauger_2,iauger_3,iapump_1,iconveyor_1,itconveyor_1,ifiller_1,ifiller_2,ifiller_3,igate_1,igate_2,icement_m_1,icement_m_2,iadditions_m_1,ifillers_m_1,iwater_q_1,ifconveyor_2,irconveyor_2,imcontainer_1,ihumidity_1 )
  instances += imitations 

plc.run( instances= instances, ctx=globals() )
