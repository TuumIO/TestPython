import os, sys
host = "192.168.1.1"
os.system("ping " + ("-n 1 " if  sys.platform().lower()=="win32" else "-c 1 ") + host)
