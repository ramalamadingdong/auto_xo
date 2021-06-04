import re
import gspread
import datetime
import ast


gc = gspread.service_account(filename='creds.json')
sh = gc.open("188th Manifest")
Auto_XO = sh.worksheet("Auto_XO")

def next_available_row():
    str_list = list(filter(None, Auto_XO.col_values(1)))
    return str(len(str_list)+1)

def msgRcv (timestamp, source, groupID, message, attachments):
    print ("msgRcv called")
    message = str(message).rstrip()

    dest = str(re.findall("(?<=DEST: ).*(?=MIS)", message,re.DOTALL)).rstrip()
    miss = str(re.findall("(?<=MIS: ).*(?=NCOIC)", message,re.DOTALL)).rstrip()
    ncoic =str( re.findall("(?<=NCOIC: ).*(?=VIX 1)", message,re.DOTALL)).rstrip()
    VIX1 = str(re.findall("(?<=VIX 1: ).*(?=VIX 2)", message,re.DOTALL)).rstrip()
    VIX2 = str(re.findall("(?<=VIX 2: ).*(?=VIX 3)", message,re.DOTALL)).rstrip()
    VIX3 = str(re.findall("(?<=VIX 3: ).*(?=VIX 4)", message,re.DOTALL)).rstrip()
    VIX4 = str(re.findall("(?<=VIX 4: ).*(?=VIX 5)", message,re.DOTALL)).rstrip()
    VIX5 = str(re.findall("(?<=VIX 5: ).*(?=VIX 6)", message,re.DOTALL)).rstrip()
    sptime = str(timestamp)

    print('dest', dest)
    print('mis', miss)
    print('ncoic', ncoic)
    print('VIX1', VIX1)
    print('VIX2', VIX2)
    print('VIX3', VIX3)
    print('VIX4', VIX4)
    print('VIX5', VIX5)
    print('SP Time: ', sptime)
    try:
        n_row = next_available_row()
        Auto_XO.update('A' + n_row, str(n_row))
        Auto_XO.update('B' + n_row, str(sptime))
        Auto_XO.update('C' + n_row, dest)
        Auto_XO.update('D' + n_row, miss)
        Auto_XO.update('E' + n_row, ncoic)
        Auto_XO.update('F' + n_row, VIX1)
        Auto_XO.update('G' + n_row, VIX2)
        Auto_XO.update('H' + n_row, VIX3)
        Auto_XO.update('I' + n_row, VIX4)
        Auto_XO.update('J' + n_row, VIX5)
    except Exception as e:
        print("google sheets problem:", e)

    return

from pydbus import SystemBus, SessionBus
from gi.repository import GLib

bus = SessionBus()
loop = GLib.MainLoop()

signal = bus.get('org.asamk.Signal')

signal.onMessageReceived = msgRcv
loop.run()
