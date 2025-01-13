#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Coded By ARON-TN
# Don't Change copyright Mother Fucker :)
# Tunisia Coderz
# Tool Finished In : 01:22 10/03/2019
# Tool Fixed in : 15:33 10/06/2019
import os, socket, threading, base64, datetime, sys, ssl, imaplib, time, re, uuid

try:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
except:
    print("\033[91mERROR :| \nContact ARON-TN AS u LIKE !\033[00m")

msg0 = "\033[91m########## verified Your modules ########"
for i in msg0:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.02)

try:
    import queue
except ImportError:
    print("\033[91m[\033[92m?\033[91m] Installing queue Module\033[00m")
    if os.name == 'nt':
        try:
            os.system('C:\\Python27\\Scripts\\pip2.exe install queue')
            import queue
        except:
            print("Install Python-Pip Sir")
            input('')
    else:
        try:
            os.system('pip2 install queue')
            import queue
        except:
            print("\033[91mTry To Install pip2 For Your Devices And Try 'root@usr:~$ pip2 install queue'\033[00m")

try:
    import requests
except:
    print("\033[91m[\033[92m?\033[91m] Installing requests Module\033[00m")
    if os.name == 'nt':
        try:
            os.system('C:\\Python27\\Scripts\\pip2.exe install requests')
        except:
            print("Install Python-Pip Sir")
            input('')
    else:
        os.system('pip2 install requests')

try:
    import colorama
except:
    print("\033[91m[\033[92m?\033[91m] Installing colorama Module\033[00m")
    if os.name == 'nt':
        try:
            os.system('C:\\Python27\\Scripts\\pip2.exe install colorama')
        except:
            print("Install Python-Pip Sir")
            input('')
    else:
        os.system('pip2 install colorama')

msg00 = "\n\033[92m##### Good Now You have all modules #####\n\033[0;96m############## Let's start ##############\033[92m\n"
for i in msg00:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.02)

# The rest of the script continues here, with the same changes applied as necessary...

