import os, sys
host = "8.8.8.8"
os.system("ping " + ("-n 1 " if  sys.platform().lower()=="win32" else "-c 1 ") + host)
