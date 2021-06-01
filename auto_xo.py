import re
def msgRcv (timestamp, source, groupID, message, attachments):
    print ("msgRcv called")
    message = str(message).rstrip()

    dest = re.findall("(?<=DEST: ).*(?=MIS)", message,re.DOTALL)
    miss = re.findall("(?<=MIS: ).*(?=NCOIC)", message,re.DOTALL)
    ncoic = re.findall("(?<=NCOIC: ).*(?=VIX 1)", message,re.DOTALL)
    VIX1 = re.findall("(?<=VIX 1: ).*(?=VIX 2)", message,re.DOTALL)
    VIX2 = re.findall("(?<=VIX 2: ).*(?=VIX 3)", message,re.DOTALL)
    VIX3 = re.findall("(?<=VIX 3: ).*(?=VIX 4)", message,re.DOTALL)
    VIX4 = re.findall("(?<=VIX 4: ).*(?=VIX 5)", message,re.DOTALL)
    VIX5 = re.findall("(?<=VIX 5: ).*(?=VIX 6)", message,re.DOTALL)
    sptime = timestamp

    print('dest', dest)
    print('mis', mis)
    print('ncoic', ncoic)
    print('VIX1', VIX1)
    print('VIX2', VIX2)
    print('VIX3', VIX3)
    print('VIX4', VIX4)
    print('VIX5', VIX5)
    print('SP Time: ', sptime)

    
    return

from pydbus import SystemBus, SessionBus
from gi.repository import GLib

bus = SessionBus()
loop = GLib.MainLoop()

signal = bus.get('org.asamk.Signal._19708232320')

signal.onMessageReceived = msgRcv
loop.run()
