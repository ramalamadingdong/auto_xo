import re
import gspread
import datetime
import ast


gc = gspread.service_account(filename='creds.json')
sh = gc.open("Trip Tickets")
Auto_XO = sh.worksheet("Auto_XO")

def next_available_row():
    str_list = list(filter(None, Auto_XO.col_values(1)))
    return str(len(str_list)+1)

def msgRcv (timestamp, source, groupID, message, attachments):

    print ("msgRcv called")
    message = str(message).rstrip()

    if message.isdigit():
        try:
            Auto_XO.update('K' + message, "RETURNED")
            signal.sendMessage("Welcome Back!!", [], [source])
        except Exception as e:
            print("google sheets problem:", e)
            signal.sendMessage("Needs Debugging " + str(e), [], ['+17272186609'])
        return

    dest = str(re.findall("(?<=DEST: ).*(?=MIS)", message,re.DOTALL)).rstrip()
    miss = str(re.findall("(?<=MIS: ).*(?=NCOIC)", message,re.DOTALL)).rstrip()
    ncoic =str( re.findall("(?<=NCOIC: ).*(?=VIX 1)", message,re.DOTALL)).rstrip()
    if ("VIX 2: " in str(message)):
        VIX1 = str(re.findall("(?<=VIX 1: ).*(?=VIX 2)", message,re.DOTALL)).rstrip()
    else:
        VIX1 = str(re.findall("(?<=VIX 1: ).*", message,re.DOTALL)).rstrip()
    if ("Vix 3: " in str(message)):
        VIX2 = str(re.findall("(?<=VIX 2: ).*(?=VIX 3)", message,re.DOTALL)).rstrip()
    else:   
        VIX2 = str(re.findall("(?<=VIX 2: ).*", message,re.DOTALL)).rstrip()
    if ("Vix 4: " in str(message)):
        VIX3 = str(re.findall("(?<=VIX 3: ).*(?=VIX 4)", message,re.DOTALL)).rstrip()
    else:
        VIX3 = str(re.findall("(?<=VIX 3: ).*", message,re.DOTALL)).rstrip()
    if ("Vix 5: " in str(message)):
        VIX4 = str(re.findall("(?<=VIX 4: ).*(?=VIX 5)", message,re.DOTALL)).rstrip()
    else:
        VIX4 = str(re.findall("(?<=VIX 4: ).*", message,re.DOTALL)).rstrip()

    VIX5 = str(re.findall("(?<=VIX 5: ).*", message,re.DOTALL)).rstrip()
    timestamp = datetime.datetime.fromtimestamp(timestamp/1000.0)
    sptime = str(timestamp.strftime("%m/%d/%Y, %H:%M"))

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
        signal.sendMessage("Trip ticket # " + str(n_row) + " filed please reply "+ str(n_row) + " when you return ", [], [source])
    except Exception as e:
        print("google sheets problem:", e)
        signal.sendMessage("Needs Debugging " + str(e), [], ['+17272186609'])
    return

from pydbus import SystemBus, SessionBus
from gi.repository import GLib

bus = SessionBus()
loop = GLib.MainLoop()

signal = bus.get('org.asamk.Signal')

signal.onMessageReceived = msgRcv
loop.run()
