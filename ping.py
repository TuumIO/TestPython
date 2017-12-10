import os
import sys
import platform
import getopt
from decimal import Decimal 

resultados = {} #Diccionario donde se guardan los resultados

def usage():
       
       print("Uso: Ping")
       print("")
       print("-i Inicio")
       print("-f Fin")
       print("-d Direccion")
       print("-h info de ayuda")

try:
       opts, args = getopt.getopt(sys.argv[1:], "i:f:d:h")

except getopt.GetoptError as err:
       print("Error: "+str(err)+", Intente -h para ayuda\n\n")
       usage()
       sys.exit(2)

for o, a in opts:
       if o in ("-h"):
              usage()
              sys.exit()
       if o in ("-i"):
              y = Decimal(a)
       if o in ("-f"):
              x = Decimal(a)
       if o in ("-d"):
              d = a
              try:
                     #i = 1
                     while y < x:
                            direc = a + "." + str(y)
                            response = os.system("ping " + ("-n 4 " if  platform.system().lower()=="windows" else "-c 4 ") + direc)
                            if response == 0:
                                   pingstatus = "Ususario Activo"
                                   resultados[y] = pingstatus
                            else:
                                   pingstatus = "Usuario no Activo"
                            y=y+1
              except:
                     print("Algo pasa aca\n")
                     sys.exit(2)

for k in resultados:
       print("Usuario: " + d + "." + str(k) + " Activo")

