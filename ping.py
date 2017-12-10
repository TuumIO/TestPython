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
              x = a
       if o in ("-d"):
              try:
                     for i < x:
                            direc = a + "." + str(i)
                            response = os.system("ping -c 1 " + direc)
                            if response == 0:
                                   pingstatus = "Ususario Activo"
                            else:
                                   pingstatus = "Usuario no Activo"
                            print(a + pingstatus)
                            i=i+1
              except:
                     sys.exit(2)
print("Listo\n")
