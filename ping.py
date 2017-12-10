import os
import sys
import getopt

def usage():
       
       print("Uso: Ping")
       print("")
       print("-f Fin")
       print("-d Direccion")
       print("-h info de ayuda")


try:
       opts, args = getopt.getopt(sys.argv[1:], "f:d:h")

except getopt.GetoptError as err:
       print("Error: "+str(err)+", Intente -h para ayuda\n\n")
       usage()
       sys.exit(2)

for o, a in opts:
       if o in ("-h"):
              usage()
              sys.exit()
       if o in ("-f"):
              x = float(a)
       if o in ("-d"):
              #try:
                     y = a
                     i = 1
                     while i < x:
                            direc = y + "." + str(i)
                            response = os.system("ping -c 1 " + direc)
                            if response == 0:
                                   pingstatus = "Ususario Activo"
                            else:
                                   pingstatus = "Usuario no Activo"
                            print(direc + pingstatus)
                            i=i+1
              #except:
                     #print("Algo pasa aca\n")
                     #sys.exit(2)
print("Listo\n")
